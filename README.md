# Calcmass
A python script to find the molecular mass in g/mol of a chemical equation  
This is forked from [Calcmass](https://github.com/konman2/Calcmass) and there're few changes here.  

## Changes
As the requests have not been merged yet, I list some of the changes here.
1. Bug fixed for multiple inputs([Link](https://github.com/konman2/Calcmass/pull/2))
2. Support for float([Link](https://github.com/konman2/Calcmass/pull/3))
3. Add an API for import convenience
## Example
Console
```
$ calcmass C3H6N6O6  
222.11634  

$ calcmass H2 O2 H2O  
H2: 2.01588  
O2: 31.99880  
H2O: 18.01528  

$ calcmass Li1.2Ni0.13Mn0.54Co0.13O2
85.28600
```
Python
```
>>> from calcmass.mass import massof
>>> massof('H2O')
18.01528
```

## Setup
To use the original version, you can check [The original repo](https://github.com/konman2/Calcmass)  

If you want to use this version, you still can download using pip.  

```
$ pip install git+https://github.com/wsyxbcl/Calcmass.git
```

for ArchLinux user, you can find ``python-calcmass`` from AUR.

