# Installation

## Requierements
<ol>
<li> Git </li>
<li> numpy </li>
<li> opencv </li>
<li> openpyxl</li>
<li> pillow</li>
<li> tkinter</li>
</ol>

## Clone Project

```
git clone https://github.com/AkashSharma786/Certificate_Sender.git

```
 


# Run the Project

### Run in terminal
```
python main.py
```
### Three popups will pop asking for 

<ol>
    <li> Path for Certificate</li>
    <li> Path for Font</li>
    <li> Path for Output Folder</li>
</ol>



### A Window  will appear for position in the certificate

    

### Treminal will ask for index of column where names are stored

### Popup will appear asking for excel file

### Terminal will ask for Three input for color red green and blue ( 0 <= num <= 255 )

### Output Will be stored in Output Folder


<hr>

# Code Expaination

<hr>

## Folder for User data

<ul>
    <li> <h2> Certificate </h2> For storing Template Certificate</li>
    <li> <h2> Excel </h2> For User data in a excel file</li>
    <li> <h2> Font </h2> Collection of fonts to be added in certificate </li>
    <li> <h2> Output </h2> For storing generated Certificates </li>
    <li> <h2> Molules </h2> Python package containing two modules
    <ul>
    <li>GetCordiates.py </li>
    <p> 
    Get cordiantes contains the function for getting  coordiates of name portion
    <br>
    position()  is called from main code
    </p>


<li>getPath.py </li>
for getting The path of folder and file
    </ul> </li>
</ul>

## File input contains three function

<ul>
<li>Get_Paths()
<p>Return tuple of 3  sting containing paths</p>
</li>
<li>Get_Paths()
<p>Return tuple of 3  sting containing paths</p>
<li>get_name_list()
<p>Returns list of Students </p>
</li>

<li>get_color()
<p>Returns tuple of 3  integer containg rgb values</p>
</li>
</li>

</ul>

# main.py assembles all the input values and generates the certificates
<hr>
<hr>
<hr>