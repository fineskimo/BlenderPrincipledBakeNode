# BlenderPrincipledBakeNode
Principled BSDF node tree that has a global switch to export textures to common PBR channels.

![preview](https://media.giphy.com/media/iemEBWNPSrmRSqUlK2/giphy.gif)

## tl;dr
* _I found out that the tool/node might not be for everyone. This is also why I hesitated with a release._
* _This work is heavily based around the workflow to bake procedrual textures to bitmaps as provided by [Aidy Burrows](https://twitter.com/AidyBurrows3D "@aidyburrows's twitter") and [Gleb Alexandrov](https://twitter.com/gleb_alexandrov "@gleb_alexandrov's twitter") here: [Using Blender Like Substance Designer](https://www.creativeshrimp.com/blender-substance-designer.html)._
* _This is inteded to be used with blender 2.8x which is still in development. Things may break.
* This thing comes __without any warranty__. Best practice is to use this on a copy on your current project first.


### Getting Started (Beginners)

0. Get and install Blender 2.8x from here: 
1. Check out [Using Blender Like Substance Designer](https://www.creativeshrimp.com/blender-substance-designer.html). first if you havent already
2. Download this github repository as zip and extract the _BlenderPrincipledBakeNode.blend_ Blender file. You do not need to open this file for now.
3. Create a copy of your desired projects blendfile.
4. Make sure, Color Management is set to Default for exporting the texture maps. (you can switch it back to filmic afterwards)
5. Append the NodeTree. 

### Getting Started 
0. Make sure, Color Management is set to Default for exporting the texture maps. 
1. Append the NodeTree. 
2. Switch all Principled BSDF shaders with the fresh appended Node Group.
3. This Node is the most powerfull if you connect it to multiple materials.
4. [Tab] into the NodeGroup and Select Your Desired Map to export with the Value Slider. 

This slider is your friend:

![An important Slider](https://media.giphy.com/media/MZGRMSlRaxgITXaxA9/giphy.gif)
