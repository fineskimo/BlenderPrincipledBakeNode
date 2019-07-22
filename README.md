# BlenderPrincipledBakeNode
Principled BSDF Node Group which features a global switch to export textures to common PBR channels.

## tl;dr
* This work is heavily based the "Baking Procedrual Textures to Bitmaps" workflow as provided by [Aidy Burrows](https://twitter.com/AidyBurrows3D "@aidyburrows's twitter") and [Gleb Alexandrov](https://twitter.com/gleb_alexandrov "@gleb_alexandrov's twitter") here: [Using Blender Like Substance Designer](https://www.creativeshrimp.com/blender-substance-designer.html).
* The Node Group is designed to be used with Blender 2.8x which is currently still in development. It may break before the final release.
* The Node Group is provided __without any warranty__. It is best practice to save a copy of your current project before use.

### Getting Started (Beginners)

1. Download and install Blender 2.8x : https://www.blender.org/download/releases/2-80/ 
2. I advise you to watch [Using Blender Like Substance Designer](https://www.creativeshrimp.com/blender-substance-designer.html) first, if you haven't already.
3. Download the github repository as a zip file and extract the _BlenderPrincipledBakeNode.blend_ file, it is not neccessary to open this file.
4. Create a copy of the project .blend file you intend to bake textures maps from.
5. Ensure Render Settings > Color Management is set to "Standard" before exporting the texture maps. (you may revert to "Filmic" afterwards).
6. Append the "PrincipledBaker" Node Group from _BlenderPrincipledBakeNode.blend_.
7. Switch all Principled BSDF shaders to the appended Node Group.
__This is super simple and preserves the original connections__

![Switch the Nodes from the Properties Panel](https://media.giphy.com/media/MbKxYGVYmc8bkg4XEV/giphy.gif)

8. This Node Group is at its most powerful when connected to multiple materials.
9. [Tab] into the Node Group and select the desired map to export using the Value slider. 



### Getting Started 
1. Ensure Color Management is set to "Standard" before exporting the texture maps. 
2. Append the "PrincipledBaker" Node Group from _BlenderPrincipledBakeNode.blend_. 
3. Switch all Principled BSDF shaders with the appended Node Group.
__This is super simple and preserves the original connections__

![Switch the Nodes from the Properties Panel](https://media.giphy.com/media/MbKxYGVYmc8bkg4XEV/giphy.gif)

4. This Node Group is at its most powerful when connected to multiple materials.
5. [Tab] into the Node Group and select the desired map to export using the Value slider. 
