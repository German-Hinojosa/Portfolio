from django.db import models

# Create your models here.
#the following has been added
class Job(models.Model): #essentially allows us to create a new class called Job
    image = models.ImageField(upload_to='images')
    #for the line above, look up model field references for the parameter
    #ImageField is a particular model from "models"
    # whenever somebody uploads an image here whenever they create a new job app
    #object, where is it that youd like for it to be saved

    #now all images and files that are uploaded as a part of models are gonna be
    #saved to one central directory and we can specify the name of that

    #but within that media folder, you can specify your own folders
    #and so for example, having a folder called 'images' might be a good idea,
    #so thats saying "inside the media folder that we are gonna create, anytime
    #someone uploads an image, it should go inside of this 'images' folder"

    #^^created a new property/variable called image (maybe can be called variable)
    #uses the "models" import from django, basically more code
    summary = models.CharField(max_length=200)
    # we dont want one of the job boxes going really big. so capped with 200
