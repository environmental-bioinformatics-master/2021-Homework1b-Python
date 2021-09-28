# Homework 1b : Codons in Python
As with the last homework, clone this repo to the HPC. By following the homework link a new repo should have been created for you with the form `2021-environmental-bioinformatics/homework1b-python-USERNAME`. This is your repository and it is how you will be submitting your homework to us. Follow the same download protocol as before. 

For this homework, you will building off of the translation exercise that we worked on in class. All your work should be done within the existing `Six-Frame-Translation.ipynb` jupyter notebook. I have provided for your reference and use the functions that we wrote in class (`get_protein` and `reverse_complement`) as well as a cell showing different ways to read in the codon tables (you might want to make this into a function).

For this homework, I want you to **comment your code very well.** For an example-- I have commented the code that we wrote in class. I expect a similar level of detail in the code you write.

## A note on Google
This is a great exercise! It is one that I did while learning to code in `python`. That being said... we are not the only ones who think this is a great exercise. So, many of the solutions to this exact problem are directly Google-able. In line with our collaboration policy, it is fine (and encouraged) to Google things like "nested for loop in Python" or "raise exception in Python". However, please don't cheat yourself out of the exercise by Googling: "Six Frame Translation Python". Again, this was designed to help you learn and you won't learn much by copying answers from the internet.

**Use your peers. Use your brain. Ask the instructors. Embrace the struggle. It is the best way to learn.**

## Getting ready to run the assignment
The first thing that you will need to do prior to attempting this assignment is create a conda environment where you will run your homework. I activate the environment we created in class (`python_lab`). We will then install a new python library (`biopython`) Run: 

```
conda install -c anaconda biopython 
```

This should install biopython into your current enviornment! 

## Starting jupyter
You are now ready to get going. As a reminder you will want to: 

1) Start up a `tmux` session. You can create a new named session (`tmux new -s name`) or attach an existing session (`tmux a -t name`). 

2) Once in the session start up your conda environment: `conda activate python_homework`

3) Make sure you are in the directory that contains the python homework assignment (i.e. has this `README.md` file). Now you are ready to start up Jupyter Notebook. On poseidon run: `jupyter notebook --no-browser` and wait for it to start and report a port number. Then, on your local machine run: `ssh -N -f -L localhost:8888:localhost:8888 USERNAME@poseidon-[l1 or l2].whoi.edu`-- filling in Username, port number and l1 or l2 as fits your situation. 

## Doing the homework

1) For the first part of the you will use the existing `Six-Frame-Translation.ipynb` jupyter notebook. There are three main questions that you will need to answer by filling in code in the provided cells. Ultimately, you will need to create the functions `six_frame`, `six_frame_specify`, `read_in_tables`, and `six_frame_changetable`. These functions largely build upon one another so you may want to copy and modify the code from the previous question. To aid in writing your answers I have provided a TESTING cell for you to use that has a series of assertion statements. If all the assertion statements pass they will not print anything and that means your code is working based on my specifications. You will be graded both on your code running and the comments you write on your code. So, please be sure to comment your code well. 

2) For the second part of your homework, I want you to write a python script called `six-frame-translation.py` that reads in a DNA sequence from a file and when provided with a translation table will produce a tab-delimited output file that lists all six frames of translation (see `Example-script-output.txt` for an example. The script should be run as follows: 

`python six-frame-translation.py SEQUENCEFILE TRANSLATIONTABLE OUTPUTFILE`

Note: for this exericse the sequence files provided are not in fasta format-- they are just raw sequence data that occur on multiple lines. 

I have provided the framework for this script already within this repo. Once you have a script that you think is working run the following commands:

```
python six-frame-translation.py sequences/DNA1.txt invert-mito output/DNA1.invert-mito.list
python six-frame-translation.py sequences/DNA2.txt invert-mito output/DNA2.invert-mito.list
python six-frame-translation.py sequences/DNA1.txt testtest output/DNA1.testtest.list
python six-frame-translation.py sequences/DNA1.txt meso-code output/DNA1.meso-code.list 
python six-frame-translation.py sequences/DNA2.txt meso-code output/DNA2.meso-code.list 
```


## Submitting your homework

Now push all your work to GitHub.

You should commit your changes to `Six-Frame-Translation.ipynb` and `six-frame-translation.py` and push them to GitHub. Then, add all the files within your `output/` folder (made above) and push them to them to GitHub. Finally, make a file called `estimatedtime.txt`; in this file please estimate how much time you spent on each of the four questions and the final script in the homework.
