# ALARM_SOUND_DETECTION_USING_TOPOLOGICAL_SIGNAL_PROCESSING

This code contains the functions we used to create the paper "Alarm Sound Detection Using Topological Signal Processing" by Tomer Fireaizen, Saar Ron and Omer Bobrowski.
The code has been written by Tomer Fireaizen and Saar Ron.

The file "diagramFromAudio.py" includes the functions that used to create persistence diagram from audio file (in mono or stereo format).
- "audio_file" receives file name and return a persistence diagram. 
- "butter_bandpass" creates a Butterworth bandpass filter
- "butter_bandpass_filter" filters a signal with Butterworth bandpass filter
- "signal_downSample" is downsampling given signal
- "import_audio_signal" importing an audio file from given address
- "cloud_from_signal" creates point cloud from a signal
- "dim_reduction" reduce the dimension of a point cloud
- "normalize_3dcloud" normalize a point cloud to have mean 0 and maximal coordinate value of 1
- "my_plot_3d" plots a 3D point cloud
- "print_diagram" prints given persistence diagram
- "print_bigger_diagram" prints the diagram with bigger dots
- "homology_from_3dcloud" is analyzing the homology of point cloud
- "create_alpha_complex" creates Alpha complex from given point cloud
- "get_betti_num" calculate the betti numbers of given Alpha complex  

The file "TopologicalFeatureExtraction.py" includes the functions that used to extract the topological features from a persistence diagram.
- "bottleneck_diagram_dist" calculates the bottleneck distance beteween two diagrams
- "diagram_threshold" eliminates cycles with lifespan smaller than given threshold 
- "ps_scoring" calculates the Periodity Score (PS)
- "qps_scoring" calculates the Quasi Periodity Score (QPS)
- "two_2ndHomology_score" calculates the Frequency Shift Score (FSS)
- "get_features" extracts the topological features from given diagram
 

The DSP features has been extracted with the code used in the paper "Detection of alarm sounds in noisy environments" (Yesurun, Carmel and Moshe, 2017).
The results of the ReliefF algorithm will be uploaded until October 10th, duo to small technical issue.

For questions, clarifications and comments, you are welcome to contact Tomer Fireaizen at the email address: tomerf@campus.technion.ac.il
