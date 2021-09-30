def audio_file(filename, filter=1):  # filename with path and all
    downsample_rate = 500
    window_size = 40
    fs, signal1, signal2 = import_audio_signal(filename=filename)
    # draw_spectogram(signal1,fs)
    if np.max(abs(signal1)) > 0:
        sig = signal1
    else:
        sig = signal2

    signal = signal_downSample(sig, downsample_rate)
    signal = butter_bandpass_filter(signal, 500, 1500, fs)
    cloud = cloud_from_signal(signal, window_size, pca_dim=3)
    cloud = normalize_3dcloud(cloud)
    my_plot_3d(cloud.T, show=True)
    first_time = time.time()
    diag = homology_from_3dcloud(cloud=cloud, max_alpha=10, print_diag=False)
    if filter == 1:
        diag = [(a, (b, c)) for (a, (b, c)) in diag if b > 0.00027 and c - b > 0.002]
    return diag, time.time()-first_time


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def signal_downSample(signal, downsampleRate):
    i = 0
    l = len(signal)
    new_sig_list = []
    while (i < l):
        new_sig_list.append(signal[i])
        i += downsampleRate
    return np.array(new_sig_list)


def import_audio_signal(filename):
    fs,data = wavfile.read(filename)
    try:
        signal1 = data[:, 0]
        signal2 = data[:, 1]
    except:
        sig = data[:]
        signal1=sig
        signal2= sig
    return fs, signal1, signal2


def cloud_from_signal(signal, window_size, umap_dim=3):
    sw = signal_sw(signal, window_size)
    cloud = dim_reduction(sw, umap_dim)
    return cloud


def dim_reduction(X_transform, umap_dim, n_neighbors=15):
    red = umap.UMAP(a=None, angular_rp_forest=False, b=None,
                     force_approximation_algorithm=False, init='spectral', learning_rate=1.0,
                     local_connectivity=1.0, low_memory=False, metric='euclidean',
                     metric_kwds=None, min_dist=0.1, n_components=umap_dim, n_epochs=None,
                     n_neighbors=n_neighbors, negative_sample_rate=5, output_metric='euclidean',
                     output_metric_kwds=None, random_state=42, repulsion_strength=1.0,
                     set_op_mix_ratio=1.0, spread=1.0, target_metric='categorical',
                     target_metric_kwds=None, target_n_neighbors=-1, target_weight=0.5,
                     transform_queue_size=4.0, transform_seed=42, unique=False, verbose=False)
    return red.fit_transform(X_transform)
def normalize_3dcloud(cloud):
    cloud = (cloud - np.mean(cloud)) / np.max(np.max(abs(cloud)))
    return cloud


def my_plot_3d(data, show=True,block=True):
    if (show == True):
        fig = plt.figure()
        ax2 = fig.add_subplot(111, projection='3d')
        ax2.scatter(data[:][0], data[:][1], data[:][2])
        plt.show(block=block)


def print_diagram(diag,type=0): # type=0 diag , type = 1 barcode
    if type==0:
        gd.plot_persistence_diagram(diag)
    else:
        gd.plot_persistence_barcode(diag)
    plt.show()


def print_bigger_diagram(diag,base_size=6,added_size=40):
    #diag = [(a, (b, c)]
    """
    'b'
    blue
    'g'
    green
    'r'
    red
    """
    plt.figure(figsize=(6,6))
    colors = ['r', 'b', 'g']
    x_lst = []
    y_lst = []
    clr_lst = []
    size_lst = []
    for i in range(len(diag)):
        point = diag[i]
        x_lst.append(point[1][0])
        y_lst.append(point[1][1])
        colr = colors[point[0]]
        clr_lst.append(colr)
        size = base_size+added_size*(point[1][1]-point[1][0])
        size_lst.append(size)
    #for i in range(len(x_lst)):
     #   plt.scatter(x_lst[i],y_lst[i],s=size_lst[i],c = clr_lst[i])
    # plot xy line
    # plot y = max(death_time of blue& green) line
    y_max = max([i for i in y_lst if i != float('inf')])
    # fix infinity
    for i in range(len(y_lst)):
        if y_lst[i] == float('inf'):
            clr = clr_lst[i]
            birth = x_lst[i]
            print(x_lst[i])
            y_lst[i] = y_max*1.01  # represents infinity in a more "convinient way"
            size_lst[i] = base_size+added_size*(y_lst[i]-x_lst[i])
    y_max = max([i for i in y_lst if i != float('inf')])

    plt.scatter(x_lst,y_lst,c=clr_lst,s=size_lst)
    left,right = plt.xlim()
    down,up = plt.ylim()
    plt.xlim(left,right)
    plt.ylim(down,up)
    plt.plot([min(x_lst)-100,max(x_lst)+100],[min(x_lst)-100,max(x_lst)+100],'k-',lw=1)
    plt.hlines(y_max,min(x_lst)-100,max(x_lst)+100,color='k')

    plt.show()


def homology_from_3dcloud(cloud, max_alpha, print_diag=True):
    alpha_asc = create_alpha_complex(cloud, max_alpha_sqrt=max_alpha)
    diag = alpha_asc.persistence()
    if (print_diag):
        gd.plot_persistence_diagram(diag)
        gd.plot_persistence_barcode(diag)
        plt.show()

    return diag


def get_simplex_num(alpha_asc):
    print("Number of simplices in the alpha-complex: ", alpha_asc.num_simplices())


def create_alpha_complex(point_cloud, max_alpha_sqrt=1):
    alpha_complex = gd.AlphaComplex(points=point_cloud)
    alpha_asc = alpha_complex.create_simplex_tree(max_alpha_square=max_alpha_sqrt)
    return alpha_asc


# homology calculation related

def get_betti_num(asc):
    betti_nums = asc.betti_numbers()
    print(betti_nums)

