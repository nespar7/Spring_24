# Mushroom Classification using Naive Bayes Algorithm
* Project 1
* Group 8
* 23BM6JP05: Akshay K
* 20CS10038: N Surya Prakash Reddy

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