import brain 
import memory


while True:
    me=input("YOU:")
    memory.add_convo("YOU",me)
    reply = brain.greet_user(me) or  brain.ask_question(me)
    print(brain.personality['name'] ,":",reply)
    memory.add_convo(brain.personality["name"],reply)

    if "bye" in me.lower():
        break


