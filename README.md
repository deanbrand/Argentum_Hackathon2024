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
`yolo val model=runs/detect/train/weights/best.pt data=data.yaml`
`yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=path/to/data/images/test save=Tr
ue`

## Depth Estimation
For the generation of depth heatmaps, the PatchFusion library is used. This part is more involved and requires the installation of another set of packages/environments, but once set up, the heatmaps can be generated through: `python ./tools/test.py configs/patchfusion_depthanything/depthanything_general.py --ckp-path Zhyever/patchfusion_depth
_anything_vitl14 --cai-mode r256 --cfg-option general_dataloader.dataset.rgb_image_dir='path/to/data/images/trai
n' --save --work-dir path/to/data/heatmaps/train --test-type general --image-raw-shape 2160 3840 --patch-split-n
um 4 4`

## Measurement Features
Wtih the bounding boxes predicted, they can be used to convert to an acutal length scale, using the `pix_to_mm.ipynb` notebook. The heatmaps can be analysed in the `nonn.ipynb`, which is also the notebook used for the construction of the non-neural network solutions (i.e. LR, SVR, RFR, GBR).

## CNN Model
The main predictor, and the most successful, is made in the `pothole_cnn_reg.ipynb`, in which the CNN is constructed and data pulled together. The pipeline is fairly simple here and self-explanatory.
