"""
import rospy
import helperFunctions as hf

class DatasetCreator:
    Creates labeled simulated dataset

    def __init__(self, model_thresh):
        self.cluster_sub = rospy.Subscriber
        self.model_sub = rospy.Subscriber
        self.cluster_msg = None
        self.model_msg = None

        # Max distance in meters between cluster and model for labeling
        self.model_thresh = 0.5

        self.dataset_df = pd.DataFrame

    def clusterCB(self, msg):
        self.cluster_msg = msg

    def run(self):
        for cluster in self.cluster_msg:
            cluster_np = numpify(cluster) ## Convert to numpy array
            attributes = hf.computeClusterAttributes(cluster_np)
            label = self.computeLabel(cluster)
            self.dataset_df.append(attributes, label) # just add new point to df

    def computeLabel(self, cluster, thresh):
        # compute distance between cluster and nearest model
        # If distance is greater than threshold

    def save(self, filename):
        self.dataset_df.to_csv(filename)

if __name__ == "__main__":
    # Make hotkey bound to save
"""
