Before we start, make sure you have a virtual environment set up and requirements downloaded. 
This is needed ONLY if you want to look at the logs of container before and after running a script:
 
1. Open the integrated terminal from the downloaded folder (right-click on the area with the docker-compose.yml file and select "open in integrated terminal"). 

2. Create a virtual environment:
   python -m venv <name of environment>

3. Activate the virtual environment:
   - Windows: <name of environment>\Scripts\activate
   - MacOS/Linux: source <name of environment>/bin/activate

4. Install the required Python packages:
   pip install -r requirements.txt


Let's have a look at how to work with Docker Container:

1. Open the downloaded content in VSCode.  

2. Look at the yaml file. Are there any problems that you can see? If yes, change them!  

3. Open the integrated terminal from the downloaded folder (right-click on the area with the docker-compose.yml file and select "open in integrated terminal").  

4. Check if Docker is installed and Docker Desktop is opened (Windows/MacOS) on your machine (check manually and also with CLI):  
   docker --version  
   docker-compose --version  

5. Optional: To download the image, write: 
docker pull <name_of_image>:<tag> (e.g., docker pull qdrant/qdrant:latest, adding the tag ":latest" is optional).  

6. To start a container, write: 
docker-compose up -d  

7. Look at the information about the container: docker ps  

8. Look at the logs: 
docker logs <id_or_name_of_container> (you can find name and tag from the results of the previous command).  

9. If you have made a virtual environment and downloaded required packages:
    Run a script: python practice.py 

10. After the script finishes, look again at the logs: 
docker logs <id_or_name_of_container>  

11. You can also check resource usage with the command: docker inspect,  
    or put the information in a file: docker inspect <id_or_name_of_container> > inspection.txt  

12. Stop the container at the end: docker-compose down  

13. You can also delete the image: docker rmi <id_or_name_of_image> 


Optional: We have also discussed the images during the presentation. There are some commands you can try with them too:

1. Open Docker Desktop (to visually see what happens to images).  
2. Open cmd.  
3. Optional: to search for the image in Docker Hub, write: docker search <name_of_image> (e.g., docker search qdrant).  
4. To download an image from Docker Hub, write...  
5. To list all the images you have, write: docker images  
6. To inspect your image, write: docker inspect qdrant/qdrant:latest  
7. To make a copy of your image, write: docker tag qdrant/qdrant:latest qdrant/qdrant:copy 
8. To delete the copy of the image, write...  

