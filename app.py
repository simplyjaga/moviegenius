from moviegenius import mgchat

print("Enter 'exit' to end the conversation")
print("Example question: Why Sivaji comes to India? in the film Sivaji.")

while True:
	user_que = input("--> User Input: ")
	if user_que.lower() == 'exit': break
	ans = mgchat(user_que)
	print(ans)

print("Bye!")
