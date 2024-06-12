# Silhouette
Make a png into various types of silhouette for scientific figures.

Background already needs to be white-ish to work.

**Usage:**

`python3 sih.3.py /Full/Path/to/Image.png`

Output (in current directory):

`Silhouette50,Silhouette100,Silhouette150,Silhouette200   .png`


**Pre-requisites**

You need:

- python3
- Pillow (e.g. from `pip3 install Pillow`)

**Tutorial:**

1. Download some png file:

`wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/NRWS_Heinz.png/800px-NRWS_Heinz.png`

2. Run the code:

`python3 silhouette.py /workspace/silhouette/800px-NRWS_Heinz.png`

3. Explore output:

You should now have 8 new pngs with varying threshold for black. 
You could amend the thresholds on line 38 of `silhouette.py`

**Gitpod enviroment (no install necessary)**

If you have a Github account you can use Gitpod to run this code:

1. Go to the follow URL:
https://gitpod.io/?autostart=true#https://github.com/chriswyatt1/silhouette/tree/main

2. In the terminal section (bottom right), you can follow the above tutorial (Steps 1-3).
