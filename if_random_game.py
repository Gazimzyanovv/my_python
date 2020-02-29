{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=int(input(\"Попробуйте угадать число в диапазоне от 1 до 4\\n\"))\n",
    "y=random.randint(1,4)\n",
    "if x==y:\n",
    "    print(\"Победа!\")\n",
    "elif x>y:\n",
    "    print(\"Повторите еще раз, это число больше\")\n",
    "elif x<y:\n",
    "    print(\"Повторите еще раз, это число меньше\")"
   ]
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
