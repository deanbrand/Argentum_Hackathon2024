from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    model = YOLO("yolov9c.pt")

    # Use the model
    results = model.train(data="data.yaml", epochs=500)  # train the model
