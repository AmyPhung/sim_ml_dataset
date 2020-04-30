# Usage
+ Start simulation `roslaunch tractor_sim_gazebo bringup.launch`
+ Record simulation dataset `rosbag record /tf /tf_static /clock /gazebo/model_states /lidarx_points`


# Testing
  + `roscore`
  + `rviz`
  + `rosbag play correct.bag` (for some reason this needs to happen beforehand)
  + `./frame_by_frame.py`


# Info
+ `datasetProcessor.py` - Filters and clusters raw lidar data, publishes clustered points
+ `datasetCreator.py ` - Subscribes to clusters and gazebo model states, computes attributes for each cluster, labels them, and saves cluster metadata for machine learning
+ `helperFunctions.py` - Provides shared functions for filtering, computing cluster attributes, visualization, and conversions between datasets
+ `FUTURE NOTEBOOK` - uses saved csv file for machine learning based on metadata

### To create dataset:
  + run DatasetProcessor on simulation data, run DatasetCreator on DatasetProcessor output
