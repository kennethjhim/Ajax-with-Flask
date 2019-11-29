blog = {
	
	'id': 1,
	'title' : 'Fucking',
	'content' : 'Story'
}

st = "my {0}, {1}, {2}".format(*blog.values())
print(st)
print(*blog.values())