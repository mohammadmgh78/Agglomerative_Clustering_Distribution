def cluster_distributions(dist_file, reg=0.5, n_clusters=None, calculate_barycenter=False, stop_threshold=10 ** -9,
                          num_of_iterations=1000, plt_dendrogram=True):
    list_sim_outputs_raw = json_content_to_list_of_lists(dist_file)
    list_base = merge_list(list_sim_outputs_raw)
    list_sim_outputs = []
    p_list = []
    for i in list_sim_outputs_raw:
        list_sim_outputs.append(density_calc(i, i)[0])
        p_list.append(density_calc(i, i)[1])
    normalized_list_sim_outputs = normalize_tuples(list_sim_outputs)[0]
    min_norm_values = normalize_tuples(list_sim_outputs)[1]
    max_norm_values = normalize_tuples(list_sim_outputs)[2]

    m = len(normalized_list_sim_outputs)
    blank_df = create_blank_dataset_with_metadata(m)
    df = fill_dataset_with_records(blank_df, make_record(normalized_list_sim_outputs, p_list))
    # Display the filled dataset
    df['data points real'] = list_sim_outputs

    fill_ot_distance(df, num_of_iterations, reg, stop_threshold=stop_threshold)

    if plt_dendrogram:
        plot_dendrogram(df, save_file=True)

    sil_values = silhouette_score_agglomerative(df)
    if n_clusters == None:
        n_clusters = sil_values.index(max(sil_values)) + 2

    columns_to_filter = [str(i) for i in range(len(df))]
    df_filter = df[columns_to_filter]
    filled_df = df_filter.fillna(0)
    matrix = filled_df.values
    diagonal = np.diagonal(matrix)
    matrix_final = matrix + matrix.transpose()

    np.fill_diagonal(matrix_final, 0)

    # Below we get the linkage matrix, which will be used in many parts
    upper_triangle_flat = matrix_final[np.triu_indices_from(matrix_final, k=1)]
    Z = hierarchy.linkage(upper_triangle_flat, method='complete')
    clusters = hierarchy.fcluster(Z, n_clusters, criterion='maxclust')

    df['cluster'] = clusters
    blank_df_clusters = create_blank_dataset_with_metadata(n_clusters)
    records_to_be_added = []
    for i in range(1, n_clusters + 1):
        records_to_be_added.append({'cluster num': i, 'p': 0})
    df_clusters = fill_dataset_with_records(blank_df_clusters, records_to_be_added)

    min_values_all = []
    max_values_all = []
    list_bary_X = []
    list_bary_prob = []
    list_inputs_cluster = []
    list_p_cluster_new = []
    list_sup_cluster_new = []
    list_sup_cluster_real_new = []
    for i in range(1, len(df_clusters) + 1):
        df_test = df[df['cluster'] == i]
        list_column = df_test['data points real']

        list_sim_outputs_cluster = list_column.tolist()
        min_values_all.append(normalize_tuples(list_sim_outputs_cluster)[1])
        max_values_all.append(normalize_tuples(list_sim_outputs_cluster)[2])
        list_sim_outputs_cluster = normalize_tuples(list_sim_outputs_cluster)[0]
        list_base_cluster = merge_list(list_sim_outputs_cluster)
        list_of_arrays = [np.array(inner_list) for inner_list in list_sim_outputs_cluster]
        X = np.random.rand(100, 2)
        b_list = [(np.ones(len(list_sim_outputs_cluster[i])) / len(list_sim_outputs_cluster[i])).reshape(
            (len(list_sim_outputs_cluster[i]), 1)) for i in range(len(list_sim_outputs_cluster))]
        t0 = 0.005
        theta = 0.005
        reg = 0.5
        print(list_of_arrays)
        print(b_list)
        bary_X, bary_a = find_barycenter(X, list_of_arrays, b_list, t0, theta, tol=1e-2 * 0.9, max_iter=400)
        list_bary_X.append(bary_X)
        list_bary_prob.append(bary_a)

        list_column_real = df_test['data points real']
        list_sim_outputs_cluster_real = list_column_real.tolist()
        list_base_cluster_real = merge_list(list_sim_outputs_cluster_real)

        cost_matrix_cluster = distance.cdist(list_base_cluster, list_base_cluster)
        density_list_cluster = density_calc_list(list_sim_outputs_cluster, list_base_cluster)
        list_sup_cluster_new.append(list_base_cluster)
        list_sup_cluster_real_new.append(list_base_cluster_real)
    matrices = list_bary_X
    matrices = [denormalize(matrices[i], min_values_all[i], max_values_all[i]) for i in range(len(matrices))]

    # Corresponding probability masses
    prob_masses = list_bary_prob

    df_clusters['p'] = prob_masses
    df_clusters['data points'] = list_sup_cluster_new
    df_clusters['data points real'] = list_sup_cluster_real_new
    json_inputs = dataframe_to_json(df, ['system num', 'data points real', 'cluster'])
    json_barycenters = dataframe_to_json(df_clusters, ['data points real', 'p'])
    return json_inputs, json_barycenters