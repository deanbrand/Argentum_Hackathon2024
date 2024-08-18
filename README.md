# Team Argentum Data School Standard Bank Lab Hackathon 2024
A repository containing all code produced and pipeline used in the Stellenbosch University School of Data Science and Computational Thinking Standard Bank Lab Hackathon 2024 focussed on pothole fixing with AI.

# Structure
In this repository there are a few files and notebooks in the pipeline that seem a bit chaotic and not well organised. There is some method to the madness. The code was run on different computers and with mixed data directories and with different python versions at points so it is difficult to run all of it as-is, sorry about that. The data that would've been included was structured something like
```
good_data
  data
    heatmaps
      train_s
      val
      test
    images
      ...
    labels
      ...
    measurements
      ...
  train_s_processed.json
  val_processed.json
  test_processed.json
  train_s_labels.csv
  val_labels.csv
  test_labels.csv
```

## Data Analysis
The file `01eda.ipynb` deals with the initial data analysis where the labels and images are correlated and re-filed in a way that can be used later. Also here that the bounding box annotations are cleaned up by replacing all L2 labels with L1 because L2 seems useless and troublesome to me.

## Bounding Boxes
Now with clean data that can be fed into a YOLO model, the test image boxes can be predicted. To train the YOLO model, the `main.py` and `data.yaml` files are used. In the correct environment with `ultralytics` installed, the `main.py` file can be run. From here the best model can be chosen from the best train detection weights. To run the validation and predictions, respectively, the following commands are used:
`yolo mode=val model=/path/to/best.pt data=data.yaml`
`yolo mode=predict model=/path/to/best.pt data=data.yaml`
