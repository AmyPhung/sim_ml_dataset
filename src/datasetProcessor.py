"""
import helperFunctions.py as hf
import rospy

class DatasetProcessor:
    Filters and clusters raw lidar data, publishes clustered points

    def __init__(self, debug=False, rviz=True,
                 gnd_thresh=0.5, env_thresh=20, min_pts=10):
        self.debug = False
        self.rviz = True

        # Min height - filter out ground points (in meters)
        self.gnd_thresh = gnd_thresh

        # Max distance - filter out environment (in meters)
        self.env_thresh = env_thresh

        # Min points - filter out clusters without enough points
        self.min_pts = min_pts

        self.lidar_msg = None
        self.cluster_msg = None  # make cluster custom message?

        self.lidar_sub = subscriber
        self.cluster_pub = publisher
        if self.rviz:
            self.bbox_pub = publisher

    ------------------------

    def lidarCB(self, msg):
        self.lidar_msg = msg

    def processLidar(self):
        lidar_base_link = ## Convert lidar message to base link coords
        lidar_np = np.convert(lidar_base_link) ## Convert lidar msg data to np array
        gnd_filtered = hf.filterGround(lidar_np, self.gnd_thresh)
        env_filtered = hf.filterEnvironment(ground_filtered, self.env_thresh)
        clusterPoints(env_filtered)

    def clusterPoints(points):
        run 2d clustering (return x,y,z,cluster_num)

        if self.debug:
            hf.visualize2DCluster
        if self.rviz:
            bbox = hf.visualize3DCluster
            self.bbox_pub.publish(bbox)

        filtered_clusters = hf.filterClusters(clusters, self.min_pts)
        hf.formatCluster()
        publish cluster

    def run(self):
        rospy.spin()
        self.processLidar()



    if name == main
        dp = DatasetProcessor
        while ros is not shutdown
            dp.run


    ------------------------
    cluster:
        points
    """
