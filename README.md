# SortingAlgorithmVisualizer
Program to visualize sorting Algorithms

<h3>1.Introduction:</h3>

   #####  1.1 - purpose
    
        In the need to develop my programming and skills and with the help of my best professor, I have built an simple program
        to visualise sorting algorithms making them easier to understand
<h3>2.Getting Started:</h3>

   ##### 2.1 - Installation Instruction
   
        Python language and some python libraries listed:
            - Tkinter, to install type : "pip install tkinter" in your python terminal

            - Matplotlib, to install type: "pip install matplotlib" (altho it is preffered to download it from their website)

            - numpy, to install type: "pip install numpy"
        and you should be good to go 
   ##### 2.2 - Quick Start
        launch the file in any text editer and start it, a microsoft window should pop up and thats the program itself
<h3>3.Usage:</h3>

   ##### 3.1 - How to use
   
        the program is very simple and straight forward its divided into two parts a graph on the right and a simple GUI on the
        left to control the graph I call it the toolbar
        
   ##### 3.2 - The GUI:
   
        - The Graph: there is nothing interactive on the right part of the window (the graph part) purely visual. Altho the right part is where
        all the visuals happen, the graph will change and update showcasing the sorting algorithms at work

        - The Toolbar: the tool bar is where all the fun happens, its divided into two parts the sorting algorthims buttons and animation control
        the buttons on the sorting algrithms part are divided into:
            - Selection sort: pressing this button will make the graph on the right start to sort following the selectionsort algorithm.
            - Bubble sort: pressing this button will make the graph on the right start to sort following the selectionsort algorithm.
            - Insertion sort: pressing this button will make the graph on the right start to sort following the selectionsort algorithm.
            - Quick sort pressing this button will make the graph on the right start to sort following the selectionsort algorithm.
            - Merge sort: pressing this button will make the graph on the right start to sort following the selectionsort algorithm.
        the second part called "Animation control" is responsible for controlling the graph itself and the buttons are as follow
            - Pause: when pressed stops the animation all together, incase the user needed to change the size of the graph or just choose 
            another algorithm
            - Reset: this button is pretty simple, it just rearranges the graph randomly getting ready for a new sort
            - entry/generate: in the entry box you enter the number of bars you need in the graph then you press "generate" and the amount typed in
            shoul be generated in the graph
            
   #####  3.3 - Input/Output Test:
    
        The User can start by pressing any algorithm button and the grapgh will start sorting, if the user felt like pausing and changing the algorithm
        then he should press pause and choose another algorithm or he can also reset the graph to start  on a clean slait
        in the Size entry the user can input the number of bars he would like and press generate and the graph will update
<h3>4.Code Structure and Architecture:</h3>

   ##### 4.1 - Overview:
    
        The code is divided into 5 main parts:
            - The initialization of the graph
            - The defining of the the animation control Buttons
            - The sorting algorithms
            - The tkinter skeleton and widgets
   ##### 4.2 - The initialization of the graph
        main matplotlib function , the setup or the array the bars the GUI container and color map
   ##### 4.3 - The defining of the the animation control Buttons
        the reset function rearranges the array generating a new graph.
        the pause button stops any animation happening globally.
        the generate function remaps the entire array and also generates a new graph.
   ##### 4.4 - The sorting algorithms
        those are divided into two parts algorithms with helper functions and vice-verse.
            a. algorihms without helper functions:
                two functions exist here a starter function that starts the animation when the button is pressed and the sorting algorithm itself
                such sorting algrithms dont need a generator function for the animation to start simply by including the "len(arr)" in the generator
                parameter is sufficient for the animation to conclude
            b. Algorithms with helper functions
                due to the complexity of such algorithms. "len(arr)" is not sufficient to act as a generator, a special function is needed specifically
                to be used as a generator and the as the one before the functions are the same , a animation starter and a the sorting algorithms functions
                
    

                
