"""
-------------FILTERING-------------------------
def filterGround(points, ground_height):
    Args:
        points (np array): Numpy array containing points to be filtered
            (in base_link tf)
        ground_height (float): Height to filter out (in meters)
    return filtered_points

def filterEnvironment(points, max_distance):
    Args:
        points (np array): Numpy array containing points to be filtered
            (in base_link tf)
        max_distance (float): Distance to filter out (in meters)
    return filtered_points

def filterClusters(clusters, min_pts):
    Args:
        clusters (list): List of clusters to be filtered
        max_distance (float): Distance to filter out (in meters)
    return filtered_clusters


-------------CLUSTER ATTRIBUTES--------------

def computeClusterAttributes(points):
    Args:
        points (np array): Numpy array containing points from one cluster

-------------VISUALIZATION-------------
def visualize3DCluster(clustered_points):
    Args:
        clustered_points (DataFrame): pandas dataframe containing the
            columns x, y, z, and cluster_num

    for cluster_num in clustered_points["cluster_num"].unique():
        cluster = clustered_points[cluster_num]
        compute bbox parameters
        return rviz bbox message

def visualize2DCluster(clustered_points):
    plot clustering in matplotlib (plot with color mapped to cluster_num)


----------------DATA CONVERSIONS---------------
def cluster2clusterMsg():

def bbox2RvizMsg():
"""
