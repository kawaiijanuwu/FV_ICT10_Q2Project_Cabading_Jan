from pyscript import document

#str
name = "Jan Immanuel Diaz Cabading"
section = "Grade 10 - Sapphire"

#tuple
hobbies = ("Sleeping", "Volleyball", "Basketball", "Reading")

#list
interests = ["Philosophy", "History", "Theology"]
interests.append("Biology")

#sets
sports = {"Volleyball", "Basketball"}
subjects = {"Philosophy", "Theology"}
likes = sports.union(subjects)

# put bold
info = f"""
<p class="mb-2"><strong>Name:</strong> {name}</p>
<p class="mb-2"><strong>Grade & Section:</strong> {section}</p>
<p class="mb-2"><strong>Hobbies:</strong> {hobbies[0]}, {hobbies[1]}, {hobbies[2]}, {hobbies[3]}</p>
<p class="mb-2"><strong>Interests:</strong> {", ".join(interests)}</p>
<p class="mb-2"><strong>Things I Like:</strong> {", ".join(likes)}</p>
<p class="mb-0"><strong>Favorite Quote:</strong> "Nothing but you, Lord"</p>
"""

#display

document.getElementById("creatorInfo").innerHTML = info