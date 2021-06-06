<h1 align='center'>Docker Cheat Sheet</h1>

### Images and Container

* ```sh 
  docker build .  #Build a Dockerfile and create your own Image based on the file
  ```
  * ` -t NAME:TAG `  #Assign a NAME and a TAG to an image
  
* ```sh 
  docker run IMAGE_NAME  #Create and start a new container based on image IMAGENAME 
  #(or use the image id)
  ```
  * ` --name NAME `  #Assign a NAME to the container. The name can be used for stopping and removing etc.
  * ` -d `  #Run the container in detached mode
  * ` -it `  #Run the container in "interactive" mode
  * ` --rm `  #Automatically remove the container when it's stopped

* ```sh 
  docker ps  # List all running containers
  ```
  * ` -a `  #List all containers - including stopped ones
  
* ```sh 
  docker images  #List all locally stored images
  ```
  
* ```sh 
  docker rm CONTAINER  # Remove a container with name CONTAINER 
  #(you can also use the container id)
  ```
  
* ```sh 
  docker rmi IMAGE  #Remove an image by name / id
  ```
  
* ```sh 
  docker container prune #Remove all stopped containers
  ```
  
* ```sh 
  docker image prune #Remove all dangling images (untagged images)
  ```
  * ` -a ` #Remove all locally stored images
  
* ```sh 
  docker push IMAGE #Push an image to DockerHub (or another registry) - 
  # the image name/tag must include the repository name/ url
  ```
  
* ```sh 
  docker pull IMAGE #Pull (download) an image from DockerHub(or another registry) - this
  #is done automatically if you just docker run IMAGE and the image wasn't pulled before
  ```
### Data and Volumes

* ```sh 
  docker run -v /path/in/container IMAGE #Create an Anonymous Volume inside a Container
  ```

* ```sh 
  docker run -v some-name:/path/in/container IMAGE #Create a Named Volume (named some-name ) inside a Container
  ```
 
* ```sh 
  docker run -v /path/on/your/host/machine:path/in/container IMAGE  #Create a Bind
  #Mount and connect a local path on your host machine to some path in the Container
  ```
 
* ```sh 
  docker volume ls #List all currently active / stored Volumes (by all Containers)
  ```
 
* ```sh 
  docker volume create VOL_NAME #Create a new (Named) Volume named VOL_NAME . 
  ```
  
* ```sh 
  docker volume rm VOL_NAME  #Remove a Volume by it's name (or ID)
  ```
 
* ```sh 
  docker volume prune #Remove all unused Volumes 
  ```
