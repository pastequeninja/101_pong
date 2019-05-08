## MAKEFILE
## EPITECH PROJECT, 2018
## 101_pong 
## File description:
## Adam Djebar - Mai Ly Lehoux
##

MAKE	=	make

PYCACHE	=	src/__pycache__/

RM	=	rm -rf

NAME	=	101pong

SRCS	=	src/usage.py \

LN 	=	ln -s

$(NAME):
	$(LN) $(SRCS) $(NAME)
fclean:
	make clean
	$(RM) $(NAME)
clean:
	$(RM) $(PYCACHE)

re:	fclean
	make
