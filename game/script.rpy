
define lucky = Character("Lucky")
define you = Character("[player_name]")
define bento = Character("Bento")
define boss = Character("Boss")

init:
    image lucky = "lucky.png"
    image bento = "bento.png"
    image boss = "boss.png"
    image dreamscape = "dreamscape.jpeg"
    image bedroom = "bedroom.jpeg"
    image work = "work.jpeg"
    image apartment = "apartment.jpeg"


default hooky = False
default romance_bento = False
default romance_lucky = False

label start:

    scene dreamscape with dissolve
    "..."
    "Thank you for coming. I really do appreciate it."
    $ player_name = renpy.input("What is your name?")
    "I see. Hello, [player_name]."
    "You should wake up. You're going to be late for work."
    jump waking

label waking:
    scene bedroom with dissolve

    you "...Ugh..."
    you "...9:43?!? Crap, I am gonna be late..."
    you "...but I'm so sleepyyy...."

    menu:
        "Go to work!":
            you "I really should go... better late than never, right?"
            you "Plus, maybe she'll be there!"
            scene black with fade
            jump work
        
        "Stay home!":
            $ hooky = True
            you "I haven't called out in a while... I guess I'll treat myself, just for today!"
            you "Maybe I can hang out with Lucky later!"
            scene black with fade
            jump bedrot

label work:
    scene work
    you "Wow! I can't believe I'm only 37 minutes late!"
    you "And it's really slow, so the boss won't be too mad at me!"

    show bento
    bento "Wow, I didn't think you were coming in today!"
    bento "Which would've been a bummer... we haven't worked together in so long!"

    you "(OMG! She's here! And she's so... beautiful!)"
    you "(I've worked at this damn coffeeshop for 3 years and have yet to tell her how I feel...)"
    you "(Lucky always says I just need to ask her out... but how could I ever have a shot with her?)"
    you "(What should I say?!)"

    menu:
        "I want you.":
            bento "You want me to what?"
            you "Umm... never mind... (Why did I say that?!?!?)"

        "(Try making a joke to impress her)":
            you "Hey, knock knock---I mean who---umm, I mean---"
            you "(Shit, what do I say!!! I don't know any joke!!!)"
            bento "You okay there, [player_name]? Just take a deep breathe..."
            "She gently shushes you, which calms you down yet makes you feel worse at the same time."

        "Haha yeah that's crazy...":
            bento "Yeah!! I'm just glad you actually showed up!"
            you "(Why am I trying to be all nonchalant?!)"
    
    you "Has the boss said anything? About me being late?"
    bento "Dude, she totally no-showed too. You could've gotten away with skipping today."
    bento "Hah, I kinda thought you somehow already knew and that's why you weren't coming in!"
    you "Haha... no..."
    bento "Not that it really matters. It's been sooooooo boring!"
    bento "Hey, what do you say we blow this popsicle stand?"
    you "What? This is a coffeeshop."
    bento "A metaphorical popsicle stand, [player_name]!"
    bento "If you wanna keep sitting here and doing nothing, I'm also down. But I think we could get away with ditching too!"
    bento "So? What'cha think?"

    menu:
        "Sure! Let's ditch!":
            $ hooky = True
            bento "Hehe, I knew you were a rebel deep down! Let's go hang at the mall!"
            you "(I hope this wasn't a mistake...)"
            jump after_work
        
        "Let's just hang out here!":
            bento "You're probably right... Hey, let's at least put the TV on, okay?!"
            you "Yeah, sounds good!"
            you "(I hope I didn't disappoint her...)"
            jump after_work

        "I'm going home dude":
            bento "What? You're leaving?"
            bento "I guess that's fair... I can hold down the fort, okay?"
            you "(Yeah, whatever...)"
            jump end
    
    label after_work:
        you "(Bento and I hung out together for the rest of the day! I still can't tell if she likes me..."
        you "...but either way, I'm really glad I went to work today! I feel like we really bonded!)"
        show bento

        bento "Thanks for hanging out with me today, [player_name]! I really had a lot of fun!"
        
        if hooky:
            bento "I just hope no one came in... especially the boss..."
            you "Yeah, that wouldn't be great if she found out..."
            bento "It'll be okay, [player_name]. We're in this together."
            "She pats you on the back, and your heart starts racing."
        else:
            bento "I would've been soooo bored without you here! Nobody even came in!"
            you "I know! Good thing I didn't skip, right?"
            bento "Yeah, I don't know what I would've done without you, [player_name]!"
        
        bento "Hey, would you want to hang out again sometime?"
        you "Oh! Umm, yeah! What would you wanna do?"
        bento "I don't know... we could go out for dinner, or go to the aquarium..."
        bento "Look, [player_name]... I really like you. Do you want to go on a date?"

        menu:
            "Ummmmm yes!":
                $ romance_bento = True
                bento "Oh my gosh! Really?!? Yippee!!!!"
                you "Yayyyyy!!! (OMG, is any of this real?!?!)"
            
            "Nah...":
                bento "...Oh... I'm really sorry... I should've known..."
                "You open your mouth to respond with words of encouragement, when..."
        
        you "Umm, do you hear that?"
        bento "That... snorting sound?"
        you "It's getting closer, right?!"
        
        show boss

        boss "ARF! ARF! *SNORT* *SNEEZE*"
        you "Oh!! Hi Ms. Boss! (WHAT IS SHE DOING HERE!!)"
        bento "Hey there Boss!! *nervous laugh*"

        "The Boss clears her throat and catches her breath."
        boss "Hi guys! Sorry about that. You know how hard it is to breathe sometimes."
        you "Haha, yeah, totally..."
        boss "Well, how was it today? Did you delight our customers? That's our job, remember, girls?"
        bento "Well, actually, it was pretty slow today..."
        boss "Oh... was it...?"
        you "Yeah, no one came in the entire time I was here, Boss. I'm sorry."
        boss "..."
        boss "..."
        boss "..."
        boss "F*** my life, man. Why do I even bother doing Anything. Stupid stupid stupid"
        bento "Hey, it's okay, Boss. People love our coffee!"
        you "Yeah, it's really good! We're just a bit undergound, you know? Not much of a customer base yet."
        you "(...even though we've been open for years...)"
        boss "...that's it! Girls, tomorrow I want you two to get out there and advertise!"
        you "How, Boss?"
        boss "I don't know! Just bring people in, please! I put my life savings into this hellhole, and by God I will make a profit!"
        boss "Have a good night, you two! Get to work tomorrow!"
        hide boss with dissolve

        show bento 
        bento "Well, I guess I'll see you tomorrow then, right [player_name]?"

        menu:
            "I'm not showing up LOL":
                bento "You're not?!? The Boss will be crushed! Did you see how sad she looked?"
                bento "Come on, you gotta come in tomorrow! Don't make me do it alone!"
                if romance_bento == False:
                    you "No, dude, I am not coming in. Sorry."
                else:
                    you "Okay, okay, I'll come in! See you tomorrow, Bento."
                    bento "See ya, [player_name]!"

            "Yes!!!":
                if romance_bento == False:
                    bento "...okay. See you then."
                else:
                    bento "Yay! But tomorrow is NOT our date, okay?! I'll take ya somewhere real cool!"
                    you "Hehe, okay! (OMG!)"
        
        hide bento with dissolve
        "And with that, you head on back to your house. You can't wait to tell Lucky about the crazy day you've had!"
        return

    label bedrot:
        you "Dude, I need to get rid of my phone. I'm so bad about doomscrolling."
        scene bedroom
        you "Ughhhh... what time is it? It's only been a few minutes, right?"
        you "I've been in bed for 4 hours?!?! I need to get up!"
        you "Eek! My head hurts..."
        jump living_room
    
    label living_room:
        scene apartment
        you "The sunlight is literally blinding right now... I feel like crap..."
        show lucky
        lucky "Hey!! What have you been up to, roomie?"
        you "(Ughhh I'm too tired for this... she's always so energetic...)"
        you "Bedrotting... I don't feel so good."
        lucky "Omg me too! Wanna couchrot? It's better for you!"

        menu:
            "I'm going back to bed bruh":
                lucky "Oh, okay! Let's hang out later though!"
                you "(Sure, whatever...)"
                scene black with fade
                jump end

            "Yeah sure!":
                lucky "YAY! I love when we hang out, [player_name]!"
                lucky "Also, there's donuts in the microwave. Take one!"
                you "Thanks, man!"
                you "(...am I blushing? Must be the headache...)"
                scene black with fade
                jump hanging_out
    
    label hanging_out:
        "A few hours later..."
        scene apartment
        "You and Lucky have been playing video games mindlessly and eating donuts all day. How wonderful!"
        show lucky with dissolve

        lucky "...Yeah, I can't believe you didn't know about that game mechanic."
        you "I just don't understand how it works or why anyone thought a breeding daycare was a good idea."
        lucky "It's for the nerds that want to create the most competitively viable team possible dude."
        you "Sounds like you're one of them."
        lucky "Maybe I am... what's it to you?!"
        "Lucky flashes a quick smile before focusing her attention back on the game. Your heart races a little bit."
        you "(Lucky is a lot of fun to hang out with. I should try to be more social...)"
        lucky "Yay! I won! Yippeeeeee!!!!"
        "She stands up and starts dancing before sitting down a bit closer to you than before."

        you "Bro that was so lame! I think you cheated."
        lucky "You're just mad I won!"
        "The two of you laugh before Lucky turns to you, eyes cast low."

        lucky "I've had a lot of fun hanging out with you today, [player_name]..."
        lucky "You know, I thought you didn't like me for a while. I thought you thought I was too energetic and cute and were jealous!"
        you "(...What?)"
        lucky "But now I know you're just kind of shy! And that's okay! It's cute, actually."
        you "(Cute?!?!)"
        lucky "Hehe, look at you now, blushing and everything! So, what do you say? Wanna go on a date?"

        menu:
            "But we're roommates...":
                lucky "That makes it all the better! We can hang out all the time!"
                you "(I don't know if that logic makes much sense...)"
            
            "Sure!":
                $ romance_lucky = True
                lucky "YAYYYY!!!"
                you "YAYYYYY!!!!"
            
            "Ewwwww":
                lucky "Oh..."
                you "Yeah... sorry bruv."
        
        lucky "Do you hear that?"
        you "Hear what?"
        lucky "Someone's at the door! I'll get it!"
        
        hide lucky with dissolve
        show boss

        boss "So, [player_name], you hate me."
        you "Eeek! No, not at all! I wasn't feeling good---"
        boss "Save it! You're fired!"
        "Strangely, this doesn't bother you too much."
        you "Okay, Boss. I'm sorry."
        boss "Hmph!"

        hide boss with dissolve
        show lucky

        lucky "That's tough. I'm sorry, [player_name] :("
        you "It's okay... I didn't like my job too much anyways."
        you "I'll start applying to other places tomorrow."
        lucky "Okay... wanna play more video games?"
        you "Duhhh!!!"
        return

    label end:
    "You weren't feeling super social today, so you just decide to go back to bed and get some sleep."
    "The Boss probably won't be too happy, but who cares?"
    "Such is the life of a sleepyhead barista."
    return