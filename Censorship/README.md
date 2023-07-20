
# Censorship

This challenge is a pyjail, our objectif is to print the flag.

The program allows us to run the code we want, but our code can't containe the words "flag" or the letter "e","t" or the characthere " \ \ " 

So we can't we just type in "print(flag)".


## 

We notice that the program start with the ligne : 

```
for _ in [flag]:
```

This means that the variable _ hold the value of the flag. 

So by calling locals()["_"] we can have access to the flag.

But we can't print it yet.

##

We notice that the program provided, has one print in it : 

```
except Exception as err:
            print(err)
```
We need to trigger an error that will return the value of the flag as err.

We can do that by inputing the following code to the program :

```
d = {}; d[locals()["_"]]
```

With this we get the flag. 

##

Or we can just use the code : 

```
d = {}; d[_]
```

