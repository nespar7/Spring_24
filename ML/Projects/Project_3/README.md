# Airline Passenger Segmentation using Complete Linkage Divisive (Top-Down) Clustering Technique
* Project 3

# Improvements:
In the divisive clustering part, I used flat clustering algorithm(K-means) by mistake which was not what was asked in the question.

The correct algorithm is to find a leading point(farthest point from all points) from each cluster, and then divide the cluster into two clusters based on the leading point. This process is repeated until we reach k clusters.

`
while len(clusters) < k:
    max_dist_cluster = -1
    for cluster in clusters:
        find the leading point in the cluster and update the max_dist_cluster if the distance is greater than the previous max_dist_cluster

    divide the max_dist_cluster into two clusters based on the leading point

    update the clusters list
`

# Running instructions:

## Colab, VSCode, Jupyter Notebook

Please change the data_path variable in the notebook to the path where the mushrooms.csv file is stored.

## Terminal

We are going to use nbconvert to compile the notebook and run inlines. 

Please install nbconvert using the following command:

```
pip install nbconvert
```

Then run the following command in the terminal:

```
jupyter nbconvert --execute --to notebook --inplace Group8_MCNB.ipynb
```