# Flask YOLOv5 Microservice

This project is a Flask microservice that detects objects in images using YOLOv5. You can send Base64 encoded image files to an API in JSON format to receive the detected objects.

## File Structure
```
├── images
│   ├── train.jpg
│   ├── zidane.jpg
│   ├── cat.jpg
│   └── bus.jpg
├── venv
├── .dockerignore
├── app.py
├── classes.yaml
├── docker-compose.yaml
├── Dockerfile
├── yolov5s.pt
├── requirements.txt
└── README.md
```
### Installing Required Libraries ###

### 1. Creating and Activating a Virtual Environment

# First, we need to create a virtual environment to isolate our dependencies. To create a new virtual environment:
```
    bash
    python -m venv venv     
```
# 1. To activate the virtual environment:
```
    bash
    source venv/bin/activate  # macOS or Linux
    .\venv\Scripts\activate   # Windows
```
# 2. Installing Requirements

# To install the dependencies:
    bash
    ```
    pip install -r requirements.txt
    ```
# 3. Deactivating the Virtual Environment

# To deactivate the virtual environment when we are done:
    bash
    ```
    deactivate
    ```

#### Base64 Conversion: ###
Open the jpg_to_base64.py file and enter the name of any photo from the images directory. Once you enter the name, the Base64 encoded string of the photo will be saved in the encoded_images directory as encoded_image_<name>.txt (where <name> is the name you entered).

#### File Structure After Base64 Conversion ####
```
├── encoded_images
│   ├── encoded_image_<name>.txt
│   └── encoded_image_<name>.txt
├── images
│   ├── train.jpg
│   ├── zidane.jpg
│   ├── cat.jpg
│   └── bus.jpg
├── venv
├── .dockerignore
├── app.py
├── classes.yaml
├── docker-compose.yaml
├── Dockerfile
├── yolov5s.pt
├── requirements.txt
└── README.md
```

### Running the Flask Application: ###
# Run the app.py file and use the following command to verify that port 5000 is active:
python app.py

# Then, open a new terminal or Bash window and run the following curl command:
bash
curl -X POST -H "Content-Type: application/json" -d "{\"image\": \"$(cat encoded_images/encoded_image_<name>.txt | tr -d '\n')\"}" http://localhost:5000/detect/<label>

When using this command, replace <name> with one of the photo names from the images directory and <label> with any object you want, provided it is listed in the classes.yaml file.

### Result Format: ###
The result returned by the API will be in the following format:
{
    “image”: “iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=”,
    “objects”: [
        {“label”: “person”, “x”: 12, “y”:453, “width”: 10, “height”: 40, “confidence”: 0.6},
        {“label”: “person”, “x”: 33, “y”: 25, “width”: 8, “height”: 26, “confidence”: 0.82}
    ],
    “count”: 2
}
### Docker Usage: ###

# To Create the Docker Image:
bash
docker build -t flask-yolov5 .

# Running the Docker Container:
bash
docker-compose up

## Test Scenarios
Since the Base64 encoded form of the image is very long, the image output in the following results is a representation.
# Cat:
bash
curl -X POST -H "Content-Type: application/json" -d "{\"image\": \"$(cat encoded_images/encoded_image_cat.txt | tr -d '\n')\"}" http://localhost:5000/detect/cat
{
    “image”: “iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=”,
    "count": 1,
    "objects": [
    {
        "class": 15,
        "confidence": 0.6566872596740723,
        "name": "cat",
        "xmax": 1142.6358642578125,
        "xmin": 65.4117660522461,
        "ymax": 455.3864440917969,
        "ymin": 135.58189392089844
    }
  ]
}
# Zidane:
bash
```
curl -X POST -H "Content-Type: application/json" -d "{\"image\": \"$(cat encoded_images/encoded_image_zidane.txt | tr -d '\n')\"}" http://localhost:5000/detect/person
{
    “image”: “iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=”,
    "count": 2,
    "objects": [
    {
        "class": 0,
        "confidence": 0.881052553653717,
        "name": "person",
        "xmax": 1141.8446044921875,
        "xmin": 742.9747314453125,
        "ymax": 720.0,
        "ymin": 48.39556884765625
    },
    {
        "class": 0,
        "confidence": 0.665813148021698,
        "name": "person",
        "xmax": 715.6621704101562,
        "xmin": 123.02410888671875,
        "ymax": 719.723876953125,
        "ymin": 193.28732299804688
    }
  ]
}
```
# Bus
Since this photo includes a person, I will configure the system to detect all objects instead of specifying a <label>.
bash
```
curl -X POST -H "Content-Type: application/json" -d "{\"image\": \"$(cat encoded_images/encoded_image_bus.txt | tr -d '\n')\"}" http://localhost:5000/detect
{
    “image”: “iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=”,
    "count": 5,
    "objects": [
    {
        "class": 0,
        "confidence": 0.8966754078865051,
        "name": "person",
        "xmax": 810.0,
        "xmin": 671.8377075195312,
        "ymax": 878.4814453125,
        "ymin": 395.2808837890625
    },
    {
        "class": 0,
        "confidence": 0.8693941235542297,
        "name": "person",
        "xmax": 346.1246337890625,
        "xmin": 220.75494384765625,
        "ymax": 867.2079467773438,
        "ymin": 408.21343994140625
    },
    {
        "class": 0,
        "confidence": 0.8506025671958923,
        "name": "person",
        "xmax": 247.87301635742188,
        "xmin": 49.313446044921875,
        "ymax": 912.3284912109375,
        "ymin": 389.7433166503906
    },
    {
        "class": 5,
        "confidence": 0.8504515886306763,
        "name": "bus",
        "xmax": 809.9509887695312,
        "xmin": 12.897674560546875,
        "ymax": 789.3175659179688,
        "ymin": 223.16925048828125
    },
    {
        "class": 0,
        "confidence": 0.5373988747596741,
        "name": "person",
        "xmax": 67.82601928710938,
        "xmin": 0.043187856674194336,
        "ymax": 875.2823486328125,
        "ymin": 552.5025024414062
    }
  ]
}
# Train
{
    “image”: “iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=”,
    "count": 1,
  "objects": [
    {
        "class": 6,
        "confidence": 0.8062382936477661,
        "name": "train",
        "xmax": 516.5650024414062,
        "xmin": 54.77414321899414,
        "ymax": 347.1490173339844,
        "ymin": 210.81942749023438
    }
  ]
}
```
Developer Notes:

This project uses the YOLOv5 model for object detection. You can find the trained weights of the model in the file yolov5s.pt in the project directory. To convert images to Base64 format and send them to the API, you can use the jpg_to_base64.py file.

After creating these documents, you can proceed to use Git for managing version control of your project.

### Git Usage:

1. ## Creating and Cloning a New Git Repository ##
```
    bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/user/project-name.git
    git push -u origin main
```

2. ## Creating a New Branch and Making Changes ##
```
    bash
    git checkout -b new-property
```
3. ## Committing Changes ##
```
    bash
    git add .
    git commit -m "Add The New Property"
```

4. ## Merging the Branch into the Main Branch ##
```
    bash
    git checkout main
    git merge new-property
```

5. ## Pushing Changes to GitHub ##
```
    bash
    git push origin main
```
By following these steps, you can document your project and manage it efficiently with Git.
