run: 
	python src/main.py

production:
	python src/main.py


#? git
save:
	git add . && git commit

ready:
	git add . && git commit && git push

