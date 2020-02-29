{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "л?то\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Введите пропущенную букву е\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Победа!\n"
     ]
    }
   ],
   "source": [
    "List=[\"самовар\",\"весна\",\"лето\"]\n",
    "x=random.choice(List)\n",
    "y=random.choice(x)\n",
    "z=x.find(y)\n",
    "print(x[0:z]+\"?\"+x[z+1:])\n",
    "m=input(\"Введите пропущенную букву\")\n",
    "if y==m:\n",
    "    print(\"Победа!\")\n",
    "else:\n",
    "    print(\"Увы!Попробуйте в другой раз!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
