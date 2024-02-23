import text2emotion as te

# Testing text2emotion

mixedEmotions = """As the sun set behind the horizon, casting hues of orange and pink across the sky,
Emily stood alone in the empty park, her heart heavy with a tumultuous mix of emotions. 
Sadness weighed on her chest like a leaden anchor, memories of lost loved ones flooding her mind, 
tears threatening to spill from her eyes. Yet, amidst the sorrow, there flickered a glimmer of happiness, 
a bittersweet reminder of cherished moments shared with those now gone. Anger surged within her too, 
fueled by injustices endured and betrayals suffered, simmering beneath the surface like a dormant volcano, 
ready to erupt at any moment. Caught in this whirlwind of conflicting feelings, she closed her eyes, 
allowing the gentle breeze to caress her cheeks, seeking solace in the ephemeral beauty of the fading day"""

happy = "I am very excited and happy"

sad = "I am very sad about my food being cold"

angry = "I am angry I cannot nap"

#Call to the function
print(te.get_emotion(mixedEmotions))
print(te.get_emotion(sad))
print(te.get_emotion(angry))