import os

# Directory to save the Markdown files
md_dir = 'C:/Users/akrat/Downloads/HerDeadVoiceWs'

# Ensure the markdown directory exists
os.makedirs(md_dir, exist_ok=True)

# Sample content for the poems
poems = [
    {
        'title': 'Her Untold Silent Screams',
        'author': 'Abhinav Patel',
        'content': """Butterflies in her dreams were replaced by fear  
Life looks like a dark, miserable road without cheer  
She holds this emptiness that can't be filled  
And there is desolation that veils the glinted field

As she stands paralyzed and strengthless  
Victim of sexual violence makes senseless  
Still, she gathers all her courage and says a prayer  
That justice will cure her inner dullness, despair

But she knows deep down that she's not to blame  
For the heinous acts inflicted on her frame  
It's not her fault that someone chose to harm  
And leave her with these scars so deep and stark

She deserves to be heard, to be believed  
And for the perpetrator to be rightly grieved  
For the justice to be served and seen  
And for her shattered soul to finally glean

The hope and light that once shone so bright  
Before the darkness took over her life  
She can reclaim her power and voice  
And take control of her own path and choice  

It won't be easy, the road ahead is tough  
But with love, support, and courage enough  
She can heal, grow, and thrive  
And create a life that feels truly alive  

She can find her faith again in the midst of the pain  
And rise above the trauma that once did reign  
She can reclaim her joy, her dreams, her hope  
And never again feel like she can't cope.  
The marks she got never gonna disappear  
Her heart trembled with fear  

No one should be reduced to this painful state  
Everyone deserves their basic human right to be safe  
That can't be bought or sold and certainly not with pain  
But strengthened within all hearts that come together and gain  
This is a fight against injustice, abuse, and crime  
Let's work towards a world where every being feels sublime"""
    },
    {
        'title': 'Her Trapped Soul',
        'author': 'Aditi Jogdand',
        'content': """She is frightened deep inside
Sorrow and hopelessness beside
Surrounded by unseen, threatening presence of them
Which brutally grabs her soul in insecurity and blame

Her smile faded away with her hopes, dreams for the future
Now just depression, anxiety that's what she nurtures
The curiosity she had as a child
Is bothering massive cyclones which aren't mild"""
    },
    {
        'title': 'Unforgotten Whirlwinds of Heart',
        'author': 'Abhinav Patel',
        'content': """Our society accused her of bringing shame
By snatching away her hopes and even name
They treated her like an animal, not a girl
Just to satisfy their barbaric thirst, biassed thinking which unfurls

The stigma surrounding sexual violence, won't let our heroine wear her
crown
She's not alone in this battle, many are enduring the same frown

It demands a change from us all to stand and put a shield against such
crime
And listen to stories of those who were affected with time
It's time for no more oppression worn as a crown
Time to lay down arm to prevent future destruction around"""
    },
    {
        'title': 'Shattered Yet Unbroken',
        'author': 'Abhinav Patel',
        'content': """The sorrow that doth plague her soul
A pain that none but she doth know
Her tears fall like summer rain
A silent plea for love in vain

What horrors must making everything endure
That she doth cry and wail so pure
A heart so burdened with such strife
That every night she takes her life

Her spirit was crushed, her body weak
No refuge left for her to seek
A victim of a cruel design
A prisoner of a world unkind

How the world hath failed this fair
Injustice doth her life ensnare
But yet she doth not yield to fate
For hope still lingers, though it's late

With every tear, she finds the strength
To carry on, despite the length
Of the path, she must tread alone
Her courage is like a diamond stone

And so she cries, with a heart so bold
For all the tales that go untold
For every soul that suffers so
For every heart that longs to know

May heaven's light guide her way
And bring her solace every day
For in her tears doth lie the power
To conquer all, in life's darkest hour"""
    },
    {
        'title': 'Darkest Sunset',
        'author': 'Abhinav Patel',
        'content': """To whom have we blamed till long ?
But the real monster continued to kill innocent souls along,
Who is to blame in this darkening time,
When so many have been subjected to crime?
For whom are we turning a searching eye,
As innocent girls must suffer and cry?

Soft innocence used as a weapon of fate,
The faces of sweet lasses filled with hate.
What fearful power doth hold up their hand,
Deeming that these young victims must endure such pain?

The blackest hearts can weaponize fear;
Young girl's lives thrown in disarray and queer.
Our world's foundations swept out from beneath;
Young girls stand broken in stagnant tears beneath.

So now we must take up justice's call;
Our souls must show that villains won't win at all!
Know this the fight for justice shall never wholly end,
Nowhere else but here good must rise upon evil bent!"""
    },
    {
        'title': 'Her Smothered Breaths',
        'author': 'Abhinav Patel',
        'content': """When she wants to speak up for her rights
She is told to silence, put out of sight
For looking outwards, fighting in vain
They're seen as monsters and scorned again.

A lifetime of violence year after year
All the while almost no one hears
The cries and voices that plead for justice
It's silenced instead with centuries of dust.

It's sad when victim is seen with shame,
As if the guilt lies in her name.

To be devastated and violated this way,
So much to bear no words can say.

So, many of us must rise to defend her right
To join forces as a mass uprising with might.
We have a moral obligation to stand strong,
And protect the victims of this horrible wrong."""
    },
    {
        'title': 'The Unshaded Darkness',
        'author': 'Aditi Jogdand',
        'content': """It is terrible to even get heard right now
Feel she feels don't deserve to even breathe somehow
She isn't sure whether she is alive or dead
The marks and memories brings her in the feeling of lying on deathbed

Each thing wasn't this way before ,
Now just darkness and self blame breaths as her soul's core

Why don't we hear and accept which is true?
Why do we need to keep her voice suppressed with fear, emotional
blackmailing's glue?
The darkness of her heart will still be the same
Or at least now, just stop this cheap game !"""
    },
    {
        'title': 'Her Broken Rise',
        'author': 'Abhinav Patel',
        'content': """The pain of a soul that's shattered,
It's pieces scattered, tattered and battered,
Feeling as though it's unworthy of breath,
Struggling to hold on, wishing for death.

The memories and marks of violence and hate,
Haunt her still, a burden too great,
Robbing her peace, leaving her in fear,
Sleeping on a bed of death, so near

No words can capture the depth of her pain,
The trauma, the shame, the loss, the disdain,
For what was done to her, without her consent,
A cruel act that no one should ever invent.

But though the darkness may seem endless,
There is hope, there is light, there is tenderness,
In the arms of those who love and support,
She can find strength, and a path to resort.

Let her know, that though it may seem dire,
She's not alone, and her pain is not entire,
For there are those who stand by her side,
Ready to help, ready to provide ,

So let us pledge to stand against hate,
To speak out against violence, to not abate,
For in the fight for justice, we shall prevail,
And the broken shall rise, and their light shall never pale.

Let's stop blaming the victims for what they wear,
Or for being out late or for being there,
Rape is not caused by the clothes they choose,
But by the rapist's desire to abuse.

Let's stop making excuses for the perpetrators,
And stop minimising the impact on the survivors,
Rape is a violent violation of consent,
And the damage it does cannot be undone or spent.

Let's educate our young ones on healthy relationships;
On consent and boundaries, on respectful trips,
For when we teach respect and empathy;
We foster a culture of love and sympathy.

Let's hold the perpetrators accountable,
And let the survivors know they are valuable,
For in the pursuit of justice, we must not rest,
Until rape and sexual violence are put to the test.

The conversation around rape must change,
To one of empathy, support, and range,
Where the survivors are uplifted and heard,
And the rapists are held accountable and deterred.

So let us reframe this conversation,
And work together for a better nation,
Where rape is seen as a grave disgrace,
And a culture of consent takes its rightful place."""
    },
  {
        'title': 'Her Crushed Wings',
        'author': 'Abhinav Patel',
        'content': """In a house that once was a home,
Lived a girl who was all alone,
Her family, the ones who should protect,
Were the ones who caused her to deflect.

Their love was tainted with violence and hate,
Their hands, once gentle, now would berate,
Her body, her soul, her every being,
Leaving scars that no one was seeing.

Her mother, once kind and caring,
Now caused her daughter much despairing,
Her father, once strong and brave,
Now made her feel like a helpless slave.

The siblings, once her closest friends,
Now joined in the abuse and its deadly ends,
Their fists and words like daggers sharp,
Cutting deep, leaving a lasting mark.

And so she wrote, in her diary each night,
Of her pain, her fear, her will to fight,
And though her family had made her feel small,
She knew that someday, she would stand tall.

For the power of words, of love, of hope,
Is a force that can help one cope,
With the darkest of nights and the hardest of days,
And bring one closer to the light's warm rays.

So though this girl's story may be tragic,
Her spirit, her words, are truly magic,
And may they inspire us all to stand,
Against abuse and hate, hand in hand."""
    },
    {
        'title': 'The Unspoken Section Of Diary',
        'author': 'Abhinav Patel',
        'content': """Innocent and pure, a child once bright,
Now a victim of a heinous plight,
Her father, brother, uncles, and kin,
Subjecting her to sin upon sin.

Where once love and safety did reside,
Now a darkness crept and did preside,
A soul defiled, a heartbroken,
By those who should have been a haven.

She wept and begged for mercy's grace,
But found no succour in this place,
For those who should have been her shield,
Had turned upon her with savage zeal.

Her spirit shattered, her trust destroyed,
Her life consumed by those who toyed,
With her innocence, her very being,
In acts that left her with no meaning.

The cruelty of these beasts so vile,
Devoid of conscience, bereft of guile,
What madness could possess such men,
To inflict such pain on kin and kin."""
    },
    {
        'title': 'Healing : Strength To be stronger',
        'author': 'Abhinav Patel',
        'content': """We stand with her, a survivor brave,

Whose strength and courage did not cave,

In the face of darkness and despair,

her will to live did not impair.

May she find peace and healing now,

May justice come with furrowed brows,

And may the scars that do remain,

Be a testament to her strength regained."""
    },
    {
        'title': 'The Murderer Industry',
        'author': 'Abhinav Patel',
        'content': """In the darkness of the night,
Her tears fall like raindrops might,
Forced into a life of shame,
Sold for men to use, a never-ending game.

Her body is not hers to own,
As she is forced to be shown,
In videos for the pleasure of men,
Her soul screams out, never to be seen again.

In the darkness of the night,
Her tears fall like stars might,
Forced to sell her body and soul,
To satisfy the desires of men, she's lost control.

Her worth is measured in dollar bills,
Her body a product for men to thrill.
No longer human, but just an object,
Her humanity stripped away, it's now the subject.
Her pain and suffering, invisible to most,
Hidden behind closed doors, it's easy to boast.

Of a world that's just, and treats all as equal,
But the reality is harsh, and its effects so lethal,
Her body is a prison, her mind a maze,
She's trapped in a world with no escape, no way to blaze,
A path to freedom, to break the chains,
Of a life that's filled with so much pain.

But hope still lingers, a flame in the dark,
A light that can guide her to a brand-new start,
To reclaim her worth, and her dignity,
To break free from this life of indignity,

The life she leads is one of pain,
Her cries unheard, her heart in chains.
Her dreams of freedom now long gone,
Her spirit broken, her light now gone.

She was once a girl with hopes and dreams,
But now she's nothing, or so it seems,
Just a commodity, a product to sell,
A victim of a world that treats her like hell.

In the shadows, she hides her face,
Her eyes downcast, her heart displaced,
For all the hurt that she has known,
Has left her feeling so alone,
And yet, she fights to find a way,
To live another day .

To heal her wounds, to mend her soul,
To rise again, and be made whole,
For she knows that she is not alone,
That there are others who have known,
The pain and sorrow that she feels,
And have risen up, to break the seals.

To fight for justice, to make a stand,
To bring an end to this wicked land,
Where girls sold, bought and used,
Their bodies broken, their spirits abused,
And though the road ahead is long,
And the journey hard, and sometimes wrong.

She knows that there is hope to be found,
In the hearts of those who are truly sound,
For in their eyes, she sees a light,
That shines so bright, and breaks the night,
And shows her that she is not alone,
That there is hope, and a way to be shown.

So let us stand, and fight for those,
Who are trapped in lives of woes,
And bring an end to this cruel fate,
And lift them up, to a better state.

In a world that's meant to be free,
Girls are trapped, they cannot flee,
From the horrors that surround them all,
Their voices silenced, their backs against the wall.

Forced into a life they did not choose,
Their bodies sold, for men to abuse,
Their dreams and hopes, now crushed and broken,
Their souls shattered, their spirits stolen.

They live in fear, and endless pain,
Their worth measured in what they can gain,
For the men who buy them, they're just a toy,
A source of pleasure, their feelings void,
Their bodies are not theirs to own,
They're used and abused, and then thrown.

Into a world of darkness and despair,
A life they never wanted, never thought was fair,
And yet, they fight to keep their flame alive,
To survive another day, and to strive,
To break free from the chains that bind,
To escape the darkness, and leave it behind.

Their spirits may be broken, but not their will,
They have the courage to rise, and to fulfil,
Their dreams of freedom, of a life they choose,
Where they're not just objects, but humans too,

So let us stand with them, and fight their flight,
To bring an end to this cruel plight.
To build a world where all can be free,
And girls can live a life of dignity,

The porn industry, where tears can be seen,
Where bodies are objectified, for all to see,
A place where pleasure is the only goal,
And the human spirit is left without a soul.

It's a world that preys on our desires,
Exploiting our needs, and fueling our fires,
With images that leave us wanting more,
And leave our souls empty, and our hearts sore,

It's a world that tells us that sex is just a game,
A game where all are players, and there's no shame.
But the reality is far from what we're shown,
For the porn industry is a world of its own,
It's a world where girls are used and abused,
Their bodies sold, and their spirits bruised,

For the pleasure of those who pay to see,
A life that's broken, and no longer free.
It's a world where consent is just a word,
And the dignity of innocent girls often blurred,

Where their worth is measured in how they look,
And their value is placed in a porn star's book,
It's a world that's built on exploitation,
A world that feeds on our fascination.

With the human form, and its many ways,
But it's a world that leaves us lost in a daze,
For we're sold a lie, that sex is just for fun,
But the reality is that our souls are done.

For the porn industry takes more than it gives,
Leaves us empty, and unable to live,
In the shadows, hidden away from the light,
Lies the dark world of porn, a harrowing sight.

Where girls are exploited and used for gain,
Their bodies violated, their souls in pain,
The industry's greed knows no bounds,
Forcing girls to perform, leaving them bound.

Used and abused, with no hope for escape,
Their dreams and aspirations, forever erased,
Raped and beaten, treated as mere objects,
Their pain and trauma, society neglects.

Chained and enslaved, their bodies for sale,
Their lives destroyed, their dignity pale,
Their cries for help fall on deaf ears,
As they're forced to face their darkest fears.

Trapped in a cycle of abuse and shame,
Their lives forever tarnished, a scarlet stain,
The porn industry's dark secrets, hidden from view,
Exploiting the weak and vulnerable, their hearts askew.

Their worth measured by their looks, and nothing more,
Their humanity is stripped away, as they're pushed to the floor.
But we cannot stay silent, we must speak out,
Against the injustice that leaves so many in doubt.

We must fight for the girls, who are left in pain,
And create a world, where their dignity can reign,

For every girl who's trapped, and every girl who's hurt,
We must stand with them, and lift them from the dirt.

And build a world, where their worth is known,
And their dreams and aspirations can forever be grown.

Let us break the prison, that hold them down,
And create a world, where their dignity will abound.

For every girl deserves a life that's free,
From the bondage of abuse, and from the porn industry,"""
    },
    {
        'title': 'The Business Of Relations',
        'author': 'Abhinav Patel',
        'content': """It starts with the birth of a girl,
Parents dread the thought of the dowry they'll swirl.

A life of struggle, of saving every dime,
Just to marry off their daughter in time.

But even then, it's not enough,
The demands keep rising, the pressure is rough.

Gold, cash, cars, and property,
All for a marriage that's meant to be.

And then the groom's family enters the scene,
With their list of demands, so obscene.

The girl's family must comply,
Or risk bringing shame to their name.

dowry, the curse on society,
A barbaric practice that must cease to be,
A system built on greed and pride,
Where girls are sold like goods to buy.

The girl's dreams and aspirations are shattered,
Her life was no longer her own, but what the groom's family mattered.

She's a prisoner, a slave to their whims,
Her worth is measured in material things.

And if she fails to meet their demands,
She's abused, tortured, and everyday harmed.

Her fate left to the mercy of fate,
Her life in tatters, her soul full of hate.

We must break the shackles of this curse,
And ensure that every girl can live without fear.

It's time for us to take a stand,
And put an end to this practice, oh so grand.

Let's empower our girls to chase their dreams,
To be fearless and confident, to achieve the impossible it seems.

Let's break down the walls of this system so wrong,
And give every girl a chance to be strong.

For it's time to rewrite the story,
Of girls who are sold, and live so sorry.

Let's pledge to make a difference,
And free every girl from this vicious sentence"""
    },
 
    {
        'title': 'Dowry The Game',
        'author': 'Aditi Jogdand',
        'content': """In a world where love and marriage should be pure,
The practice of dowry remains a stubborn lure.
A bride to be, caught up in the dowry game,
Is but a mere pawn in an unfair claim.

A father's love for his daughter, pure and true,
Should not be measured by the gifts he can accrue.
For dowry, the price tag of a bride,
Is but a cage in which her spirit will hide.

Her worth is not measured in material things,
But rather in the joy and love she brings.
Her heart's desires, her passions and dreams,
Should be the focus of the suitor's schemes.

Yet still we see the dowry system thrive,
A stain on the fabric of modern life.
The value of a woman, cheapened by this trend,
Her life's path narrowed, her choices penned.

Forced to marry someone who'll pay the price,
Her heart's desire dismissed, a sacrifice.
Her life now at the mercy of a stranger's whim,
Her spirit crushed, her future dim.

A father who cannot afford the fee,
Will surely face societal scrutiny.
A daughter who cannot find a match,
Will face ridicule and often dispatch.

"""
    },

    {
        'title': 'The Fictitious Practice To Slave innocent Souls',
        'author': 'Abhinav Patel',
        'content': """Oh, dowry, a cruel and callous game,
Bringing only misery, sorrow and shame.
A tradition that has no place in modern times,
A scourge that should be purged from all minds.

Let us all take a stand against this vice,
And raise our voices against this injustice twice.
Let us declare our love without any price,
And break the chains of this system so unwise.

For a girl should be cherished, loved and free,
To pursue her passions and her destiny.
Let us create a world where she can thrive,
A world where her worth is never based on a bribe.

So let us pledge to support our sisters dear,
And break the shackles that they live in fear.
Let us fight against this practice so severe,
And end this dowry system once and for all, my dear.

In the game of dowry, it's not just the bride who's caught,
But the groom too, unknowingly, becomes a character of the plot.
A cycle of greed and coercion that repeats over time,
It's a tradition that's deeply ingrained, a cultural crime.

Father forgets that once he too had taken dowry,
And now he's forcing his daughter to bear the same story.
The groom too, blinded by his own ego and pride,
Doesn't realise that he too is on the wrong side.

But the bride, the victim of this cruel game,
Her life is ruined, her dreams go up in flames.
She's bought and sold, her worth measured in gold,
Her happiness and well being, forever put on hold.

It's time to break this cycle of abuse and greed,
To give the bride the respect and love she needs.
A union of two hearts, based on love and trust,
Without any price tag, without any lust.

For a dowry free society, we must fight,
And embrace a new dawn, where love is the only light.
Innocent eyes, so pure and bright,
A precious life that shone so bright,

But the world was cruel and full of plight,
And darkness fell upon her like a blight.

The men around her, so depraved,
An innocent life, they so enslaved,
Their lustful hands, so cruelly waved,
And shattered her soul, as she lay there un saved.

From father to brother, uncle and friend,
Their evil ways, they did not end,
Aunts and uncles, they did offend,
And the horror continued, with no defend.
They took from her, what was not theirs,
Innocent flesh, they treated like wares,
No one to hear her, no one to care,
A life destroyed, in the hands of the snares.

And though she tried, with all her might,
To fight against the endless night,
The darkness won, and snuffed her light,
Leaving the world, in utter fright.

This is the fate, of too many girls,
Their lives destroyed, by society's whirls,
We must stand up, against these wrongs unfurls,
And protect their lives, with all our pearls."""
    },
    {
        'title': 'Her Debilitated Innocence',
        'author': 'Abhinav Patel',
        'content': """Her heart, once pure and trusting,
Was broken by a love so unjustly.
Her secrets now revealed, her fear growing,
Her studies halted, her dreams lost.

Her heart shattered as her love betrayed,
Her moments, once private, now displayed.
Her studies stopped, fear consumed her soul,
And her pain left her feeling far from whole.

Fear consumed her, her studies came to a halt,
As she struggled to regain what she once sought.
A relative offered a chance to study and grow,
But little did she know, it was a trap, a toxic show.

Her own kin, the ones she trusted, blackmailed her so,
Threatening to hurt her sister, it was a cruel blow.
Against her will, they raped her, destroying her trust,
It seemed like a never ending cycle of unjust.

She thought work would bring an escape, a new start,
But again, she was met with cruelty, tearing her apart.
Her boss saw her as inferior, just a tool to use,
Raped in the elevator, to move forward, she had to lose.

Called to the cabin, told to submit to him,
Her body was a commodity, it all seemed so grim.
A life that once had dreams and aspirations,
Now consumed by pain, violence, and frustrations.

Oh, the plight of the girl, in a society so unjust,
Where she's merely an object, to be used and thrust.
Betrayed by love, by family, by work, by all she knew,
Her spirit may be broken, but her courage will renew.

Let us raise our voice, for the girl's rights to be heard,
To stop the cycle of violence, so she can soar like a bird.
May her struggles never be in vain, may her voice be strong,
For we will fight beside her, till justice is served, till the wrong is gone."""
    },
    {
        'title': 'Unleash The Fight For Injustice',
        'author': 'Abhinav Patel',
        'content': """This is a tale that's all too real,
A story that transcends time and place,
Of pain and trauma that girls feel,
A danger lurking in every space.

It happens in homes and in classes,
With children and in neighbourhoods,
A vicious cycle that surpasses,
Any attempts to change its moods.

Ask the girls in your own abode,
And you'll find that this story's true,
The same tale that's oft been told,
Of what they've been subjected to.

The danger lurks in every corner,
A danger that's omnipresent,
A peril that's hard to conquer,
An enemy that's quite incessant.

She wonders if she'll ever feel whole again
Or if this pain will always remain
She wants justice, but it seems so far
In a world that doesn't value who they are

This is not just a story, it's a tragedy
A reality that should fill us with agony
We need to stand up and speak out
To make sure this is not what life is about
In this world, men hold the power,
And women are preyed upon each hour,

It's a scary and sad reality,
One that we must address with clarity.
My friend's message struck me to the core,
If only death was a better score,

For girls who live in constant fear,
Of being violated, with no one near.
I couldn't respond, what could I say?
When girls are assaulted every single day,
From the crowded metros to the empty alleys,
Their safety is compromised, their dignity in valleys.

Even when I accidentally collide,
With a girl who scolds, her anger I can't abide,
I know it's not my fault, but I still feel the shame,
For I know the culprit is a man who has no game.

A man who gropes, a man who leers,
A man who masturbates in public and feeds on fears,
This man is everywhere, and I am he,
A part of a society that lets him be.

He puts his hands on shoulders and waists,
He caresses backs and leaves girls disgraced,
He rubs his penis on buses, on hostel walls,
His actions leave scars, and society mauls.

He gives chocolates and shows off his status,
But when he's done, the girl's life is in hiatus,
Her dreams and aspirations shattered,
Her life forever altered and tattered.

I am ashamed, for these forms are mine,
And I know that I must draw the line,
I must be the change that the world needs,
And ensure that women's rights and safety precedes.

The suffocating girls in this society
Their plight is one that none can deny
Victims of a system that's rigged against them
Their fate determined by the whims of men

It starts with a feeling of power and control
A desire to dominate, to own, to hold
In the bed, it's not about pleasure or love
But the rush of power, the animal inside us, we shove

We're not having sex, we're showcasing our might
To prove to the world we're the kings of the night
Our girlfriends know how rough we can be
In the name of power, we rob them of their dignity

This power is not confined to the bedroom walls
It flows into the streets, into public stalls
Where men grope, touch, and harass with impunity
Their power unchecked, fueled by their masculinity

The power dynamics are clear to see
Men hold the reins, and women are at their mercy
A subtle touch, a grab, a groping hand
A constant reminder that women are not in command

The system is rigged, and the girls suffer
Every day, every moment, it's getting tougher
To exist, to survive, to thrive in a world
Where men hold all the power, and girls are left to unfurl

The power of masculinity, a force to behold
A feeling that's nurtured, from young and old
It's the feeling of control, of dominance and might
A feeling so strong, it clouds our sight

In bed, we show it off, our girlfriends know
We don't make love, we put on a show
We display our power, with every thrust
In that moment, we feel like we must

Our power cannot be contained, it spills out
Into the world, it seeks to shout
We massage arms in crowds, we slap hips
We grope breasts, it's all in our grips

We transfer our power, a subtle ritual
One that's been passed down, from time immemorial
When it cannot be contained, it seeks to reign
Over the world, it seeks to maintain

It's a poverty, a sickness that afflicts us men
We want to dominate, again and again
We deny the existence of suffocating girls
We don't care about their cries or their whorls

Our power blinds us, we can't see the truth
The harm we cause, the damage we ruth
We don't care about their pain, their fears
We revel in our power, in our leers

We must stop and listen, to their voices
We must understand, their choices
We must empathise, with their plight
We must fight for their rights, with all our might

The power of masculinity, it's time to rethink
It's time to let go, of this poisonous ink
It's time to embrace, a new way of being
One that's based on love, and true seeing

We must understand, that power is not a game
It's not something to use, to control or maim
It's something to share, to lift up and empower
It's something to use, to build and empower

In this world where masculinity is power
We dominate, we conquer, we tower
Our ego so fragile, our mind so weak
We seek validation from every girl we seek

Our inner poverty is like a disease
It dominates our actions with such ease
We think we love, but do we really?
Or are we just satisfying our own needs, really?

Our girlfriends and wives, they suffer in silence
Our domination over them, it's violence
We don't understand the situation at hand
We think consent is enough to make a stand

But have we ever asked ourselves, have we tried?
To understand the pain we cause, the tears we've dried
The girl who joined us, did she really think
That love is what we did, with consent, like a wink?

Our mindset is our biggest mistake
We can't see beyond our own ego's sake
Why wouldn't we be mad at seeing someone outside?
When we can't even understand the pain we provide

Our poverty is a curse, a plague upon us
It makes us blind, it makes us unjust
We don't see the suffocating girls in our society
We just want to dominate, in every stage and variety

But let me tell you, my fellow men
There is a way out, a way to end
This poverty that we carry deep inside
It starts with empathy, with opening our eyes wide

We must listen, we must understand
The pain that we cause, with our own hand
We must stop dominating, stop using our power
And start loving, start caring, every minute, every hour

For only then, can we truly be
The men that we aspire to see
The ones who respect, the ones who care
The ones who end this poverty, this despair.


"""
    },
    {
        'title': 'Reanalyse Masculinity',
        'author': 'Abhinav Patel',
        'content': """As I ponder on this matter,
The weight of guilt and shame
Crushes down upon my heart
For I know I share the blame.

For every time I stayed silent
When my friends spoke in crude ways
I gave them power to objectify
And prey on girls as if they're prey.

And for every time I dismissed
The cries and pleas of a victim
I contributed to a culture
That treats women as slave.

It's time to admit our faults
And take responsibility too
For the crimes and injustices
That women suffer, it's not new.

We need to raise our children right
Teach them that gender is not a divide
That every person deserves respect
And dignity, it's not something to be denied.

Let's not make girls' beauty
A means of measuring their worth
For they are more than just their looks
And their value extends far beyond the earth.

And in our workplaces and schools
Let's call out bad behaviour
And make it known that such actions
Will not be tolerated, nor ever.

For it's the little things we do
That can have the biggest impact
In changing the toxic culture
And paving the way for a better contract.

In the heat of passion, we forget
The weight of our actions, the toll they'll exact
On those we claim to love, to cherish, to protect
Our desire becomes an all consuming threat

We seek to dominate, to assert our power
To prove our manliness in that fleeting hour
We forget the purity of the moment
As we rush to leave our mark, to make it potent

But what about her, the one we claim to care for?
What about her feelings, her desires, her core?
Do we stop to ask, to listen, to understand?
Or do we plow ahead with our own demands?

We forget that love is more than just physical
It's emotional, mental, spiritual
It's a bond that goes beyond the skin
A connection that goes deep within

We forget that our actions have consequences
That our selfishness has repercussions
That the trauma we inflict is not just physical
But emotional, mental, and spiritual

We forget that love is a partnership
That it requires communication and consent
That forcing someone to do something against their will
Is not love, but a violation of their dignity and free will

It's time to wake up, to see the truth
That our actions have a ripple effect, a proof
That we are not just hurting our partners
But also perpetuating a culture that's darker

We need to educate ourselves and our children
On gender equality, respect, and consent
On the beauty and worth of every human being
Regardless of their gender or anything

We need to stand up and speak out
Against stalking, harassment, and assault
To be allies, not bystanders
To break the silence, to be the difference makers

It's time to redefine what it means to be a man
To reject the toxic masculinity that's a sham
To embrace a new definition of strength and power
One that's based on respect, love, and honour

So let's start with ourselves, with our own actions
Let's make a change, let's have a reaction
Let's love our partners in their fullness
Without reducing them to objects of our lust and roughness.

In this world of chaos and pain,
Where oppression seems to reign,
We must look within ourselves,
And change the way we think and feel.

For too long we've let our desires,
Lead us to commit heinous crimes,
Against those who are weaker,
And those who cannot fight.

But now it's time to take a stand,
To change our ways, to understand,
That love is what we truly need,
Not violence or dominance or greed.

We must learn to control our urges,
And see the value of consent,
For it's not about what we want,
But about mutual respect.

Let's show love to our wives and partners,
Not try to force them to our will,
For the power of love is greater,
Than any momentary thrill.

And as we make these changes within,
We'll send a better energy to the world,
A light of hope that shines so bright,
For every boy and every girl.

So let's replace oppression with love,
And send a message to the world,
That we can be better, we can change,
And create a better world for all.

"""
    },
    {
        'title': 'The Deals Of Soul',
        'author': 'Abhinav Patel',
        'content': """In a dark and desolate world,
A girl's innocence was sold and hurled,
Into a life of misery and pain,
A life where she has no control or gain.

She was forced to sell her body,
To satisfy the whims of those who were gaudy,
Her tears went unnoticed and unheard,
Her voice was silenced and blurred.

Forced into a life of shame,
Her body used for others' gain.
A victim of society's neglect,
Her future now an uncertain prospect.

Her eyes once held a spark of hope,
Now empty and devoid of scope.
Her spirit broken, her will now weak,
She carries on, day by day, week by week.

No one hears her silent cries,
No one sees the pain in her eyes.
Lost in a world of darkness and despair,
She longs for someone to care.

But no one comes to her aid,
As she continues to be betrayed.
Sold and used like a commodity,
Her life now a tragic anomaly.

She was treated like a mere object,
Used and abused without any respect,
Her dreams shattered, her hopes dimmed,
Her body violated, her soul trimmed.

Her life was no longer her own,
A victim of the vicious and the unknown,
Her screams echoed in the night,
As she fought against this vile plight.

But her cries fell on deaf ears,
And her pain remained unseen and unclear.
For in a world where lust rules all,
A girl's worth is measured by how much she can enthrall.

So let us not turn a blind eye,
To the pain of those who are forced to comply,
Let us rise up and fight against this plight,
And give these girls the chance to see the light.

For they deserve to be loved and cherished,
Not bought and sold like some perishable merchandise,
Let us stand with them and be their voice,
And help them break free from this cruel choice.

For every girl forced into prostitution,
We must show love and compassion.
We must lift them up and offer a way,
To a future full of hope and light of day.

In the depths of our souls, we find a truth,
A truth that transcends our daily pursuit,
A truth that speaks of love and unity,
Of empathy, compassion, and community.

But in this world, so full of noise and distraction,
We often forget this essential satisfaction,
We chase after power, wealth, and fame,
Ignoring the cost, neglecting the pain.

We live in a society that values success,
But success at what cost? What do we address?
Do we measure our worth by the money we earn,
Or by the kindness we show, the lessons we learn?

It's time for us to awaken, to open our eyes,
To see the world through a new set of ties,
To embrace our humanity, our shared existence,
And recognize that we all need assistance.

For in the end, it's not about what we gain,
But about how we live, how we manage the strain,
And if we can find it within ourselves to be kind,
Then a better world we'll surely find."""
    },
    {
        'title': 'Be The Wise Change',
        'author': 'Abhinav Patel',
        'content': """In this world, so vast and wide
There are those who can't hide
From the eyes that follow their every move
And the hands that invade their groove

These girls, so innocent and pure
Are subject to a world so obscure
Where stalkers lurk in every corner
And their peace of mind they must barter

In a world where power reigns supreme,
The innocent are prey to a sinister scheme.
Girls, vulnerable and pure of heart,
Are subject to society's oppressive art.

Stalkers lurk in every corner,
Their lecherous gaze like a foreigner,
Invading the privacy of a girl's mind,
Leaving behind scars, hard to unwind.

In a society that glorifies masculinity,
Girls are made to feel like a liability.
Their intelligence, their achievements, all ignored,
Their worth measured by their beauty, adored.

They are told to dress modestly, stay inside,
And yet, they are blamed if they are assaulted, defied.
Their freedom curtailed, their choices denied,
Their lives controlled, their hopes denied.

It's time for us to wake up and see,
That a girl's life deserves to be free.
Let's build a world where girls can thrive,
Where their dreams are realized, and they can come alive.

Innocent hearts, pure and young,
Their fate decided before they've sprung,
Forced into unions they don't desire,
Their dreams and hopes now set on fire.

In the depths of the human soul,
Lies a darkness we cannot control,
A force that seeks to dominate,
And dictate the fates of those we hate.

To be married against one's will,
Is a fate too cruel to instill,
A life of misery and despair,
A life that no one should have to bear.

Society's expectations, traditions to uphold,
But at what cost, their hearts sold?
Chains of oppression, they're made to wear,
Their freedom and choice, stripped bare.

Parents, guardians, don't you see,
The damage that you're causing, can't you set them free?
Marriage should be a bond of love and trust,
Not a means to satisfy society's unjust.

Let their hearts and minds be free,
Let them choose their own destiny,
Forced marriages, a tragedy in disguise,
Let's break these chains, and let them rise.

Let them bloom and grow with love,
Let their hearts soar and reach above,
For in their happiness lies our own,
Let's break these chains, and let love be known.

Forced into marriages, they have no say
Their lives become a game, a mere play
Their future determined by the hands of another
Their fate sealed, as if under a spell or a curse

To some, it may seem a cultural norm
But for these girls, it's a life so forlorn
Their dreams and aspirations forever lost
As they become a possession, at a great cost

No longer able to live life on their own terms
Their desires, their passions, all go unconfirmed
Their voices silenced, their spirits broken
Their hearts heavy, and their eyes a token

Of the pain that they carry deep inside
As they continue to live in this forced ride
Their emotions run high, but they cannot be expressed
Their thoughts and opinions, forever repressed

Forced into a world, they didn't choose to belong
Their future dictated, as if they don't belong
Their lives reduced to mere commodities
To be traded, bought, and sold like properties

Their bodies are a gift, but not theirs to give
Their choices, their rights, taken away like a sieve
Their worth, their value, reduced to a price
Their dignity and self worth, taken without a fight

It's time for a change, for a world so new
Where girls are respected, and their dreams come true
Where they can decide, their own fate and destiny
Where their voice is heard, and they can truly be free

Let's break this cycle, this age old tradition
And let girls live a life with ambition
Where they can thrive, and not just survive
And be the best versions of themselves, so alive.

Let's empower them with knowledge and skill
So that they can achieve what they truly will
Let's support them, and give them a chance
To shine bright and make their own stance

Forced marriages, a thing of the past
Let's make a change, that will forever last
Let's give these girls the gift of life
And let them be the ones to decide."""
    },
    {
        'title': 'Muted Voices, Stolen Dreams',
        'author': 'Abhinav Patel',
        'content': """Abhinav, a philosopher and thinker,
In India, he dwelled, seeking to uncover
The truth behind the trials of women,
And the injustices they face, one after another.

He saw the pain of dowry, a burden to bear,
A price to be paid for a daughter to wed,
A cycle of debt, oppression, and despair,
That kept women under society's tread.

But even beyond this, a more heinous crime,
Forced marriage, a horror that he could not condone,
Girls robbed of their youth, of their freedom and time,
Their futures sealed, before they have even grown.

Abhinav saw the shackles of tradition,
The weight of customs and ancient norms,
That kept women in a state of submission,
Their dreams and desires considered lesser forms.

He saw the fear in their eyes, the pain in their hearts,
The hopelessness that engulfed them like a shroud,
As they were stripped of their agency, their essential parts,
Treated like property, disallowed to be proud.

But Abhinav did not simply observe and despair,
He spoke out against the oppression of girls and women,
He called for change, for a world that is fair,
Where every person's worth is considered a given.

Abhinav, with a heavy heart,
Sees the suffering of these girls, torn apart,
And so, he speaks out against this cruel fate,
Demanding change, before it's too late.

He called for education, for opportunities,
For girls to be treated as equals and more,
To be allowed to thrive and fulfil their destinies,
To be valued for their minds, their talents, their core.

And though the road is long, the journey fraught with strife,
Abhinav remained committed to the cause,
He would not give up, not while there was still life,
For he knew that true change would only come from his pause.

So let us all take up this banner, this call to arms,
To fight for the rights of girls and women, to make their voices heard,
For the time is now, to end all these harms,
And create a world where every person is valued, cherished, and revered.

In a world of ancient customs and traditions,
There exists a practice that defies all reason,
A bond that's formed without consent or volition,
A forced marriage, a union without passion.

Girls are often the ones who bear the brunt,
Of this archaic custom, this barbaric stunt,
Forced into a life they never chose,
Their dreams and aspirations forever froze.

Their fate is decided without their say,
Their hearts and minds forced to obey,
Their lives forever altered and changed,
In a world where their voices are estranged.

The love they seek is deemed unnecessary,
Their desires and wishes viewed as secondary,
Their worth measured in their domesticity,
Their dreams of education and freedom, mere frivolity.

Forced into a marriage they never wanted,
Their souls and spirits forever haunted,
By the injustice of their stolen fate,
By the loss of their autonomy, the cost of their state.

Their identities stripped, their agency taken,
Their potential squandered, their will forsaken,
Trapped in a life they never chose,
Their souls forever scarred, their hearts never close.

Forced marriages of girls, a practice so archaic,
A societal ill, a custom so tragic,
A violation of human rights, a crime against humanity,
A blight on our world, a stain on our dignity.

Forced marriages of girls, a tragedy so real,
Let us work together, let us heal,
A world that's broken, a world that needs repair,
Let us build a world, where every girl is free and fair."""
    },
    {
        'title': 'A Cry for Freedom',
        'author': 'Abhinav Patel',
        'content': """Oh, the weight of her burden, so heavy to bear,
The scars and the pain, the constant despair,
The feeling of worthlessness, the struggle to survive,
The fear that engulfs her, the wish to not be alive.

Her heart aches with every breath that she takes,
As the memories flood in, and the pain awakes,
The bruises and the cuts, the wounds that won't heal,
The trauma that lingers, the torment she feels.

She wonders if she'll ever be free from this pain,
If she'll ever be able to break from this chain,
If there'll ever be a day when she can smile,
When she can breathe with ease, and rest for a while.

But hope seems so far away, like a distant dream,
As she struggles to escape, from this endless stream,
Of violence and abuse, of horror and pain,
Of a life that she didn't choose, but was forced to sustain.

Yet, in the depths of her despair, a flicker of light,
A glimmer of hope, that shines so bright,
A strength that rises, a spirit that soars,
A will to survive, that refuses to be torn.

For she knows deep down, that she is not alone,
That there are others who stand with her, who have shown,
That there is a way out, that there is a path,
To a life that's worth living, to a future that's bright.

So she takes a deep breath, and finds the strength within,
To rise up and fight, to break from this sin,
To reclaim her life, to find her way,
To a world that's safe, where she can stay.

For she knows that she deserves to live,
To be happy, to be free, to receive,
Love and kindness, and a life that's true,
To be herself, and not just make it through.

And so she takes another step, and another,
Towards a life that's full, and a future that's brighter,
Towards a world where no one will have to feel,
Like they don't deserve to breathe, or to heal."""
    },
    {
        'title': 'Disrupt this Cycle',
        'author': 'Abhinav Patel',
        'content': """Why blame the girls for what they bear,

For crimes against them, so unfair?
Why shift the blame to those in pain,
And punish them again and again?
Why force them to hide and stay,
When justice should pave the way?

Why victim blame when we should see,
The root of the problem in society?

Why ask what she was wearing or doing,
When the real issue is power and thinking?
Why make her feel guilty and shamed,
When the perpetrator should be blamed?

Why do we teach our daughters to fear,
Instead of teaching our sons to hear,
Their no's, their boundaries, their rights,
And respect them without any fights?
Why do we make the victim suffer,
When it's the rapist who deserves the buffer?

Why blame the girls for what they bear,
When they're the ones who are truly rare,

Strong and brave to face the world,
Despite the stigma and insults hurled?
Let's change our perspective and start,
To support and uplift every broken heart."""
    },
    {
        'title': 'Love Language Of humanity',
        'author': 'Abhinav Patel',
        'content': """In love's embrace, a higher force,
That binds two souls in its pure course,
With every breath, with every kiss,
A union formed, in timeless bliss.

But when the force is one of power,
And love is stripped of its sweet flower,
What's left is but a hollow shell,
Of agony and endless hell.

To force oneself on one's own spouse,
Is to rob them of their very house,
Of dignity and self respect,
And leave them feeling so abject.

For love is not just physical,
It's spiritual and magical,
And when we seek to dominate,
We seal our own unhappy fate.

Let's cherish those we love and hold,
With tenderness and hearts so bold,
For in that love, we find our peace,
And all our doubts and fears are released.

For only then can we truly see,
The beauty of love's majesty
Love, a word so pure and divine
Yet humans distort it, commit a crime
Forcing themselves on their beloved spouse
To fulfill desires, they cannot arouse

Lust and pleasure, they seek to gain
Ignoring their partner's hurt and pain
Forgetting the bond they once shared
Leaving their love and respect impaired"""
    },
    {
        'title': 'Love : the power of healing',
        'author': 'Abhinav Patel',
        'content': """Innocence is stolen, hearts left scarred
As selfish actions leave their love marred
Trauma inflicted, wounds deep and raw
Mental state shattered, a painful flaw

Consequences of such actions severe
Ruining lives, breeding hate and fear
It's time to understand love's true meaning
To cherish it, and end this darkening screening

Let's embrace love in its purest form
Respect, care and trust, a new norm
Let's put an end to forced desires
And reignite the passion of love's fires.

It's easy to be swayed by desires so strong,
To demand your own pleasure, ignore what's wrong.
But remember, your wife is not just for sex,
She's a partner in life, who needs love and respect.

If you force her to do what she doesn't want,
You'll inflict wounds on her spirit that will always haunt.
She'll be filled with anger, sorrow and pain,
And never be able to trust you again.

So it's better to start loving her, body and soul,
And appreciate the moments that make you whole.
For love is not just about physical pleasure,
It's about deep connections that you'll always treasure.

If you cherish her and make her feel secure,
She'll open up to you and love you even more.
Her heart will be filled with warmth and affection,
And she'll find solace in your loving attention.

But if you abuse her, she'll feel trapped and alone,
A victim of your selfishness, powerless and unknown.
The trauma you cause will never fade away,
And haunt her for the rest of her days.

So choose your path wisely, and treat her with care,
For love and respect are what your wife deserves to share.

Remember, her heart is fragile, and needs your embrace,
So cherish her always, and let love fill every space.
The call for gender equality,
A noble cause we must uphold with sincerity
For too long women have faced the brunt
Of societal norms and cultural stunt

Their beauty deemed attainable or unattainable
Reduced to objects, often found vulnerable
But who will show compassion to their plight
When their attackers are filled with spite

It starts with teaching our children well
About gender equality, a message we must tell
No difference between sister and friend
For the plant has different flowers, yet they blend

At work, we must stop our friends
From behaving like stalkers, for it offends
A behaviour that can lead to dire consequences
Or teach others to follow, and repeat offences

Looking at girls is one thing,
But staring and doing X rays, an alarming fling
We must acknowledge the difference
And ensure that it never crosses the fence

Forcing a woman to have sex against her will
Inflicts trauma and leaves a mental anguish
Rather, let love and compassion reign
For such moments hold their own significance, don't constrain

Let's shun the momentary pleasure
That leaves behind an emotional treasure

And understand the importance of love
That brings joy, peace, and happiness thereof

The consequences of ignoring their plight
Are terrible, a black mark on humanity's sight
Let's show empathy, love, and respect
For women, who deserve nothing but the best."""
    },
    {
        'title': 'Not a Feminine light',
        'author': 'Abhinav Patel',
        'content': """She is not the representation of feminine grace

Whose cruel acts leave innocence in disgrace
No sympathy we offer for her ill willed deeds
As we stand with the purity that victim bleeds

Girls are not merely a word, a symbol to uphold
When their innocence is sacred, we must staunchly uphold
Where they are oppressed, we must rise to support
Where they are exploited, we must strive to thwart

Those who aid in exploitation, they do not belong
For feminine nature sings a different song
Of compassion, kindness, and empathy in kind
And to those who violate it, we leave them behind

We stand with the innocent, the pure and the true
Their stories we hear, their cries we heed, we pursue
And those who dare to cause them harm or pain
We teach them a lesson, for they must not reign

The feminine soul is a light to behold
And those who tarnish it, leave their own stories untold
For in the end, only kindness and love remain
And those who embody it, shall forever reign."""
    },
    {
        'title': 'Comprehending Humanity',
        'author': 'Abhinav Patel',
        'content': """The power that we hold within,
As men, it is not a thing of sin.
But when we use it to dominate,
And exploit girls, it's a cruel fate.

Our masculinity should not define,
The way we treat the feminine divine.
Sex should not be a power game,
But a moment of love, without shame.

But many men seek to assert,
Their power, making girls hurt.
They rush to see their animal side,
And ignore the purity of the moment's tide.

We use sex to show our might,
To strike a girl's vagina with our sight.
Our girlfriends know how rude we are,
In bed, we treat them like a cheap cigar.

This power transfer, when unfulfilled,
Is released in ways that should be killed.
We massage arms, slap hips and grope,
Asserting power, losing hope.

This poverty of the mind,
Is a common disease we find.
Some control it, some don't,
All want to dominate and flaunt.

Our inner poverty dominates,
Our girlfriends and wives, we deprecate.
Do we love them in those moments,
Or just use them to satisfy our elements?

Do girls think that rape is love,
When they join us, like a dove?
Have we tried to understand,
Their consent, and the power in our hands?

Our mindset needs to be questioned,
Our actions, our thoughts, our intention.
We make mistakes, we must admit,
And learn from them, to benefit.

Love should not be a power game,
But a connection that we can claim.
We must respect girls, their innocence,
And teach the cruel ones, a lesson intense.

For the word, "girl" does not define,
Their actions, their nature, their design.
We must stand with innocence,
And not those who cause turbulence

Compassion for those who abuse,
Is hard to find, impossible to choose,
Their victims, vulnerable and weak,
Are left with scars, both physical and bleak.

How can we claim to love and care,
When we inflict pain, and cause despair?
Our wives and girlfriends, whom we hold dear,
Deserve our love, and nothing to fear.

Don't put beauty in a category,
Unattainable, or too extraordinary,
Girls deserve respect, not just lust,
Treat them with kindness, not disgust.

In the workplace, stop stalking friends,
Their actions could have deadly ends,
Rapists are born, not made in a day,
Teach them now, or they'll surely pay.

Looking is fine, but don't cross the line,
Staring, gawking, is not fine,
Respect boundaries, and their privacy,
Don't reduce them to mere commodity.

Gender equality is a cause worth fighting,
To end the oppression, and stop the biting,
Of those who abuse their power,
And make girls' lives a living shower.

Let us stand with the innocent,
And bring to justice the malevolent,
Teach the cruel, and show them the way,
For a better tomorrow, a brighter day."""
    },
    {
        'title': 'Kindness The Ray Within',
        'author': 'Abhinav Patel',
        'content': """Kindness is a virtue that can heal,
A touch of compassion that we can feel,
It’s the balm that soothes our pain,
The ray of hope amidst the rain.

A kind word or gesture goes a long way,
It can brighten up someone's day,
It costs nothing to be kind,
But the impact it has is one of a kind.

In a world full of chaos and strife,
Kindness is the thread that binds us to life,
It’s the beacon of light that shows us the way,
The guiding force that leads us astray.

It’s easy to be caught up in our own needs,
But kindness is about fulfilling others' deeds,
It’s about lending a hand to those in need,
To help them overcome the impossible deed.

It’s the act of giving without any expectation;
Of spreading joy and love in every nation,
It’s the language that all can understand,
The thread that unites every land.

Kindness is the antidote to hate,
The medicine that cures all our fate,
It’s the force that can conquer all,
The power that can make us stand tall.

So let’s be kind in all that we do,
And spread this message to others too,
For a little kindness can go a long way,
And brighten up someone's darkest day.

The world is vast and full of wonder,
But sometimes, we're left to ponder,
What is our place in this great expanse?
What is the meaning of our life's dance?

We search for answers, high and low,
In books, in people, in places we go,
We seek the wisdom of the sages,
And look for clues in ancient pages.

But what if the answers we seek,
Are not found in words we speak?
What if the truth lies in our hearts,
In the compassion that each of us imparts?

Kindness is the key, this we know,
It's what makes our world a better show,
It's what binds us, heart to heart,
And makes us stronger, right from the start.

Kindness is not a simple act,
It's a way of life, that we must enact,
It's not just about being nice,
It's about being good, being wise.

We must be kind to ourselves first,
For it's from within that kindness bursts,
We must nurture our own self care,
And show ourselves the love we all deserve to bear.

But kindness must not stop with us,
We must spread it far and wide, without fuss,
We must be kind to those we meet,
To strangers on the street, and even those we greet.

Kindness is a powerful force,
It can change the world, without remorse,
It can heal the hurt, and soothe the pain,
And bring sunshine, after the rain.

"""
    },
    {
        'title': 'The End Of Time',
        'author': 'Abhinav Patel',
        'content': """She was pure, a delicate flower,
Until they came, with such power.
Ripped her soul, and left her bare,
In a world, that didn't seem to care.

They took her innocence, with their lust,
And left her feeling nothing but disgust.
Her screams were silenced, by their force,
As they showed her, what was their true source.

But after, when the damage was done,
She was seen, as nothing but a used one.
Blamed and shamed, for their own crime,
Her life was shattered, in no time.

They said she asked for it, with her dress,
As if that gave them the right, to express,
Their animalistic nature, without a care,
Leaving her to suffer, in despair.

But she was more than just a body,
More than an object, for their hobby.
She was a person, with dreams and goals,
A being, with a beautiful soul.

Her voice deserves to be heard,
Her pain should not be ignored.
She deserves justice, and so much more,
For the violence, that she had to endure.

It's time to change the narrative,
To stop blaming and shaming the captive.
To hold accountable, those who inflict,
And to give the survivors, the love and respect.

Let's educate, and spread awareness,
Of the horrors, that they face with fairness.
Let's stand together, as a united force,
To give the survivors, a path to recourse.

Because girls are not just used objects,
They are not just there for men's subjects.
They are human beings, with worth and value,
And it's time we acknowledge, and pursue.

Justice for the survivors, and a world of change,
Where they are seen, as more than just strange.
Where they are celebrated, for their strength,
And their resilience, goes to great lengths.

So let's stand up, and speak out,
Against this crime, that fills us with doubt.
Let's be a voice, for the ones in pain,
And let's never forget, that they are not to blame.

They say she asked for it,
Because of what she wore,
Her body was on display,
So she must have wanted more.

But did they ask her for her consent,
Or even look into her eyes?
Did they ask her how she feels,
Or hear her silent cries?

No, they took what they wanted,
And left her broken and used,
Blaming her for their actions,
As if she had nothing to lose.

But she's not a thing to be taken,
Or an object to be used,
She's a human being with emotions,
And a soul that's been bruised.

She deserves to be respected,
And to live without fear,
To be treated as an equal,
And have her voice be heard loud and clear.

We need to change the narrative,
And shift the focus to the crime,
Stop blaming and shaming the victim,
And hold the perpetrator accountable every time.

Let's teach our children about consent,
And the value of respect,
To build a world where everyone's safe,
And no one feels the need to deflect.

We can make a difference,
By standing up for what's right,
And showing love and compassion,
To those who've lost their light.

Let's stop the blaming and shaming,
And start healing from within,
To create a world where everyone,
Can live without fear and sin.

For every girl who's been violated,
And blamed for the crime,
We stand with you in solidarity,
And vow to fight until the end of time."""
    },
    {
        'title': 'Her Walk On Empty',
        'author': 'Abhinav Patel',
        'content': """She was just a child, so innocent and pure
But they took advantage, of that she was sure
It was her own family, who she trusted the most
But they abused her, and left her feeling lost

She tried to speak up, to tell someone the truth
But they blamed her, said she was being uncouth
They said she was lying, that it couldn't be true
And so she suffered, with no one to turn to

Her body felt used, like it wasn't her own
She felt dirty and ashamed, like she had grown
Into something ugly, that no one could love
She felt trapped, unable to rise above

But she was strong, despite what they had done
She refused to be a victim, to be overcome
By the pain and the sorrow, that they had caused
She chose to rise above it all, and not be paused

She sought help, from those who believed
Who listened and supported, and helped her to relieve
The burden of the trauma, that she had to bear
She found hope, and began to repair

Her shattered sense of self, and her broken heart
She learned to love herself, and to never part
From the truth of her worth, as a human being
No longer a victim, but a survivor, strong and seeing

That she deserved love, respect and dignity
And that her past did not define her, or her destiny
She rose above the shame, and the blame
And found peace, in her own name

lets strike at the root, which causes such pain
Let us be the change, and never let it happen again
Her family, who she thought would always be there,
Are now the ones who cause her despair,

Her body, once her temple, now a source of pain,
And in her heart, she bears an unending strain.
She feels lost, alone, and violated,
Wondering how her family could be so misguided,

How they could break the sacred bond of trust,
And inflict on her a lifetime of disgust.

The pain is overwhelming, her tears never ending,
As she struggles to cope with the unspeakable offending,

Betrayed by the ones who swore to love and care,
And now she's left with scars that can never be repaired.

She tries to forget, to move on and forgive,
But the memories remain, haunting her as long as she lives,
The shame, the guilt, the fear that they instilled,
All because of the evil desires they fulfilled.

She's blamed and shamed, as if it's all her fault,
For the actions of those who have no remorse or thought,

And society judges her, as if she deserves the abuse,
As if she's the one who chose to be misused."""
    },
    {
        'title': 'Her concealed wounds',
        'author': 'Abhinav Patel',
        'content': """Her cries are still untold,
And her heart so cold,
She's breathing but not air,
Broken soul and anxiety, what a mispair!

Smile , laugh were already snatched,
Those monstrous acts and expressions she watched.
Emotionlessness grabbed her soul deep inside filled with dark;
But each pain , memory were sharp,

What she did to be in this state ?
As you all said no , she was never late.

Her voice full of deep sorrow and heart full of scars ,
She is also human,Why did she got those marks ?

Her injuries are now deadly rain ;
Which not visible dont even pain.

The shine of sun is the darkest night;
But she seems normal to eye sight.

The black of complete silence is still unseen,
Why don't you hear her carefully ? She isn't a machine !"""
    },
    {
        'title': 'Innocent Heart\'s Broken Courage',
        'author': 'Aditi Jogdand',
        'content': """Her soul brutally harmed
She feels unarmed
One's heart full of love and care
Lost her courage , dare

Bearing unbearable shamefulness and self blame kills her from inside
Where there was once happiness, innocence , goals reside
The twinkling stars did hold themselves on pause
Where are those basic rights and those laws ?

Just a child small and bold
Only a gentle heart and smile that's what she hold
The little girl child called as the form of goddess durga , kaali
Why did forced her to get stuck in blame's dreadful valley

Did you thought she is voiceless , dumb object ?
Who gave you the right of her soul to dissect ?
That little girl who deserved to fly
Bothering a lot but still silent cry

She prayed that at least once you have heard
What she going through and beared
Nothing can express her trauma and that fear
Everything was clear but didn't appear"""
    },
    {
        'title': 'Broken Soul\'s Screams of Silence',
        'author': 'Abhinav Patel',
        'content': """The horror of it all, the pain that's felt
By girls who suffer in silence, as if dealt
A cruel hand by fate, left with no choice
But to endure the abuse, with no voice

It starts at home, with family and kin
The very people who should protect and win
Their trust, but instead they shatter it
Leaving the girl to suffer, bit by bit

The father who should be a source of love

Betrays her, and turns into a monster to shove
His desires onto her, without any care
For the damage he inflicts, or the scars he'll leave bare

The brother who should be a friend and guide
Preys on her vulnerability, and makes her hide
In fear and shame, as if she's to blame
For his actions that are nothing but a shame

The uncle who should be an elder to respect
Uses his power to force her, and neglect
Her cries for help, leaving her to suffer alone
Feeling helpless and trapped, with nowhere to run

And what about the mother who's supposed to care
She stands by and watches, as if it's fair
That her daughter's innocence is taken away
By those who are supposed to keep her safe and sway

The pain is unbearable, the scars deep
As the girl struggles to keep
Her sanity intact, and her will to survive
Against those who seek to take away her life

She was just a girl, innocent and pure
Until her own family made her feel unsure
Of what love really meant, of what was right
As they took from her the most sacred of light

They whispered promises of protection and care
But then violated her body, leaving her in despair
With each touch, each assault, each degrading word
They chipped away at her spirit, like a cruel, sharp sword

Her body became a battleground, a site of war
As they tore away her autonomy, her right to say "no more"
She was trapped in a nightmare, a hell of their making
And no one was there to hear her heart breaking

Her screams went unheard, her tears unseen
As they continued to abuse her, so cruel and obscene
And she wondered why this was happening to her
Why she couldn't escape, why there was no cure

For the pain that they caused, for the trauma they inflicted
As they used her body, her soul, like a toy, so unrestricted
And she felt so alone, so isolated in her pain
As they left her broken, shattered, again and again

The touch of terror, the weight of fear,
A trauma that's too heavy to bear,
A darkness that engulfs the soul,
A wound that refuses to be made whole.

The body, once a temple of peace,
Now a battlefield where violence won't cease,
The mind, once a garden of dreams,
Now a barren wasteland with endless screams.

The pain of abuse, a shattering blow,
Like a wildfire, it consumes us whole,
Like a serpent's venom, it spreads and bites,
Draining us of hope, as day turns to night.

Metaphors fail to capture the pain,
Words are powerless, as the tears rain,
Similes can't express the trauma we bear,
As we try to heal, to find some repair.

Personifying the pain, it takes on a life,
A demon that cuts us like a knife,
An enemy that we fight every day,
A shadow that refuses to go away.

The imagery, vivid, in shades of gray,
A memory that never fades away,
The scars that we bear, etched in our soul,
A tale of suffering that's yet to be told.

The symbolism, the weight of a chain,
A weight that we carry, like a ball and chain,
A prison that we cannot escape,
A sentence we serve, without any respite.

The alliteration, a sound so sharp,
A scream that we stifle, deep in our heart,
The assonance, a whisper so soft,
A plea for help, that we barely cough.

The consonance, a moan so low,
A plea for mercy, that no one will know,
The repetition, a mantra we say,
A hope for survival, day after day.

The rhyme, a melody that we hum,
A song of sorrow, that we sing alone,
The rhythm, a beat that we follow,
A dance with fear, that we cannot disown.

The onomatopoeia, a sound so raw,
A cry for help, that echoes and draws,
The hyperbole, an exaggeration so strong,
A pain that's intense, that lasts so long.

The irony, a cruel twist of fate,
A punishment we didn't anticipate,
The allusion, a reference to pain,
A history of suffering, that we can't contain.

The enjambment, a break so sharp,
A fracture that leaves us in the dark,
The caesura, a pause so long,
A moment of silence, when nothing is wrong.

The euphony, a harmony so sweet,
A healing that's slow, but sure to meet,
The cacophony, a discordant sound,
A suffering that's real, that we can't confound.

The anaphora, a repetition so strong,
A message that we want to prolong,
The epiphora, a repetition so clear,
A hope that's renewed, every year.

The symploce, a repetition so bold,
A truth that's spoken, that never grows old,
The metonymy, a name we give,
A trauma that lives, that we can't outlive.

The synecdoche, a part of a whole,
A wound that's deep, that takes its toll,
The antithesis, a contrast so stark,
A pain that's felt, that leaves its mark.

The apostrophe, a plea so loud,
A call for justice, that we shout out,
The cliché, used with irony,
A statement of truth, that's hard to see.

The pain of abuse, a burden we bear,
A story that's real, that we cannot repair,
The trauma we face, an endless fight,
A hope for justice, that shines so bright.

Innocence shattered, trust broken,
The weight of shame, a heavy token.
Silenced by fear, unable to speak,
The pain and trauma, forever unique.

A teacher's hand, a predator's touch,
The innocence of childhood, ripped asunder much.
Unaware of danger, we blindly trust,
Yet monsters lurk, waiting to pounce and thrust.

The memories haunt, never to fade,
A wounded heart, forever unafraid.
To speak out, to demand justice,
To fight for healing, amidst the chaos.

The scars remain, etched on the soul,
A reminder of a time, we lost control.
Yet within the pain, there lies a power,
To overcome the darkness, in the darkest hour.

Through metaphors and similes, we paint the pain,
The personification of trauma, the imagery of shame.
The symbolism of innocence, shattered and torn,
Alliteration of anguish, the consonance of mourn.

The repetition of sorrow, the rhythm of grief,
The rhyme of trauma, a silent, yet thundering thief.
The onomatopoeia of cries, the hyperbole of fear,
The irony of justice, a victory never quite clear.

The allusion to a world, where safety is the norm,
The enjambment of hope, where healing takes form.
The caesura of resilience, the euphony of strength,
The cacophony of outrage, the anaphora of events.

The epiphora of stories, the symploce of pain,
The metonymy of healing, the synecdoche of the slain.
The antithesis of silence, the apostrophe to hope,
The cliche subverted, a warrior refusing to cope.

The darkness of trauma, never to be denied,
Yet within the pain, there is hope, we shall abide.
For the power of healing, the strength of survivors,
Shall rise above the pain, with hope as their drivers."""
    },
    {
        'title': 'Life which is bought and sold',
        'author': 'Abhinav Patel',
        'content': """In this world of love and union
Where hearts beat with a sweet fusion
There's an ugly practice that prevails
One that leaves a trail of tears and wails

Grooms with their demands on dowry
Judging girls by their father's money
Is this what love and marriage is?
A transactional agreement with a financial twist?

Oh, the irony of it all
As love is supposed to stand tall
Above all materialistic gain
Yet, here we are, stuck in this bane

The worth of a woman reduced to her wealth
A commodity to be bought and sold by stealth
Is this what our society has become?
A place where love and compassion are numb?

Grooms with their list of demands
On cars, gold and prime lands
And if the father can't comply
The bride-to-be is left to die

Left alone to face the taunts
Of a society that wants
Nothing more than a grand show
Of wealth, power and status quo

The bride's family left in despair
Struggling to meet the groom's unfair
Demands on their financial reserves
Leaving them with shattered nerves

Oh, the irony of it all
As love is supposed to stand tall
Above all materialistic gain
Yet, here we are, stuck in this bane

Why must the worth of a woman be
Reduced to her family's property?
Why must she be bought and sold
For the sake of wealth and gold?

It's time for us to break free

From this age-old atrocity
To stand up against these demands
And take a stand for what's truly grand

Love, respect and understanding
These are the values worth demanding
In a world where the worth of a woman
Is not measured by her father's money

Dowry, the weight of gold and pride,
A burden borne by a groom's side,
A custom old, entrenched in greed,
A bartering of daughters, a heinous deed.

The price is set, a life is sold,
A daughter's worth, in coins of gold,
The groom's family, demands their right,
A sum so high, it's beyond sight.

The bride's family, bows to the demand,
For societal norms, they must withstand,
They sell their land, their savings, their all,
To ensure their daughter, never falls.

But what of love, and what of joy,
In this transaction, where's the employ?
What of the girl, and her wishes too,
Is she not worth, more than gold so few?

Her dreams are crushed, her voice unheard,
Her life is bartered, her freedom blurred,
A victim of tradition, of patriarchy,
A life bound in chains, a lifelong misery.

Dowry, a curse, a societal bane,
A custom steeped in deep-rooted disdain,
Let us break these shackles, and set her free,
And let her live, her life with dignity."""
    },
    {
        'title': 'Her Broken Wings and Healing Scars',
        'author': 'Abhinav Patel',
        'content': """Innocent children, so pure and true,
Their bodies violated, their spirits subdued.
Captivity and imprisonment, a life of shame,
Their abusers walk free, their victims to blame.

Metaphors of darkness, their souls in chains,
As they struggle to break free from the pain.
Their bodies betrayed, their trust in shattered,
Their cries ignored, their innocence battered.

Personified monsters, with evil intent,
Taking advantage of the vulnerable, with no relent.
Their twisted desires, a sickening disease,
Inflicting their trauma, with such ease.

Metaphors of fire, burning deep within,
As the victims fight back, and refuse to give in.
With courage and strength, they resist and persist,
Breaking free from their tormentors, no longer dismissed.

The imagery of struggle, a fight to survive,
Against those who seek to harm and deprive.
Their voices now heard, their stories told,
Their resilience and bravery, forever bold.

The metaphors of light, shining through the pain,
As the victims reclaim their lives again.
No longer prisoners, no longer trapped,
Their souls and spirits, forever unwrapped.

For these innocent girls, so young and small,
We must stand together, to hear their call.
To end sexual violence, to break the chains,
And give them the freedom, they so rightly claim.

Innocent girls, with hearts so pure,
Their pain hidden, but still so sure.
Tears they cry, in silence and alone,
Their hearts aching, their spirits unknown.

Their pain runs deep, like a river untamed,
Carrying with it, memories of shame.
Betrayed by those they trusted most,
Their innocence lost, a cruel cost.

Their bodies violated, their souls torn apart,
A pain so deep, it grips their heart.
Memories haunt them, day and night,
Shadows of the past, an endless fight.

The pain they carry, a burden so heavy,
Their hearts and minds, never ready.
To face the world, with heads held high,
For the pain they feel, will never die.

Society fails them, time and time again,
Blaming the victim, for the sins of men.
Their pain dismissed, their voices unheard,
A system broken, a tragedy absurd.

But still they rise, with strength and grace,
Brave warriors, taking back their space.
Their pain transformed, into power and might,
As they stand tall, in the face of the fight.
Innocent and pure, a child at play,
Her world shattered in one horrid day.

A monster lurking, a predator in disguise,
Stealing her light with sickening lies.

She trusted him, the one who stole her trust,
A vile creature of malice and lust,
He ripped away her childhood, her sense of self,
Leaving her scarred, in a state of mental health.

Her body, once a temple, defiled by sin,
The marks left behind a permanent grin,
Her pain runs deep, it's etched into her soul,
Her trauma so great, it's hard to control.

The shame and guilt that follows her around,
An unwelcome guest in her mind, always found,
The world can be so cruel and unforgiving,
Leaving her feeling helpless, barely living.

The memories linger, the flashbacks burn,
The terror and horror of that fateful turn,
The monster's voice echoes, it won't go away,
A haunting reminder, day after day.

The scars may fade, but they'll never disappear,
The pain may lessen, but it's always near,
A wound that's been opened, never to heal,
A heart left broken, unable to feel.

But hope remains, a light in the dark,
A voice that whispers, you're more than a mark,
You're a survivor, a warrior, a force to be reckoned,
A strength that's grown, from what once was beckoned.

The journey is long, the road is tough,
But she's not alone, she's got her rebuff,
A support system that's there to stay,
Helping her through, come what may.

The monster's voice grows fainter each day,
As she learns to find her own way,
Through therapy, love, and faith in herself,
She finds the courage to seek out her own wealth.

But now she finds the strength to speak,
Her story, though painful, must be seen and heard unique.

"""
    },
    {
        'title': 'She\'s Surviving the Unthinkable',
        'author': 'Abhinav Patel',
        'content': """I was a 6 year old girl, so innocent and pure,
When the world turned dark, and I was no longer sure
What was right and wrong, what was love and hate,
When the touch of a trusted hand became my fate.
He came in the night, when I was alone,
Whispering words that chilled me to the bone,
Promising me secrets that no one else would know,
But I didn't want to listen, I didn't want to go.

But he was older, wiser, and so much stronger,
And I was just a child, no match for his hunger,
So I gave in, I let him have his way,
And I felt my soul die a little every day.

For years, he took from me, what should have been mine,
My body, my mind, my spirit, he left me behind,
A shell of the girl I used to be,
Lost in a world of pain and misery.

I tried to tell someone, anyone who would listen,
But they said I was lying, that it was just fiction,
That no one would do such a thing to a child,
That it was all in my head, that I was just wild.

So I kept it inside, the shame and the fear,
Hoping that one day, the end would be near,
But the memories stayed, like a cancerous growth,
Eating away at my soul, like a terrible oath.

I hated myself, for what he had done,
For the way he had made me feel, for what I had become,
I felt dirty, tainted, and forever scarred,
And I couldn't escape the darkness, no matter how hard.

But then something changed, a spark in the night,
A glimmer of hope, a flicker of light,
I realized that I was not to blame,
That I was not the one who should feel shame.

It was him, the abuser, the monster within,
Who had committed the sin, who deserved the spin,
Of the wheel of justice, that would make him pay,
For what he had done, day after day.

And so I began to heal, to fight back,
To reclaim my life, and to attack,
The demons that haunted me, the voices in my head,
Telling me that I was better off dead.

I learned to love myself, to forgive the past,
To see the beauty in life, and to make it last,
I found my voice, my power, my strength,
And I used it to break free, to go to any length.

And though the journey was long, and sometimes hard,
And the memories still lingered, like a playing card,
I knew that I was not alone, that others had survived,
And that I could make it, if I just tried.

So here I am, standing tall, and strong,
A survivor of the abuse, a fighter for the wronged,
And though the scars still remain, and the pain still stings,
I am free, and that is all that really means.

She is a survivor, a warrior of sorts,
With scars that run deep and emotions that distort.
She has seen the worst of humanity's face,
And survived the horror of childhood's disgrace.

The memories linger, haunting her days,
A relentless nightmare that never fades.
The touch of another sends shivers down her spine,
A reminder of the violation that was once hers to confine.

The shame is a constant, a burden she bears,
A heavy weight that she cannot share.
For who could understand the pain and fear,
Of a child who was robbed of their innocence, dear?

The anger burns bright, a fire within,
Fuelled by the injustice and the world's sin.
She rails against the cruelty that she has known,
And vows to never let it define her alone.

But healing is a journey, a path that is long,
With twists and turns that leave her feeling wrong.
The triggers are many, the road is tough,
But she holds on to hope, for it is enough.

The scars may never fade, but she can choose,
To let them define her, or to let them loose.
To live a life that is rich and full,
And find the beauty in each moment, no matter how small.

She is not just a survivor, she is a thriver,
A phoenix rising from the ashes of fire.
She chooses to live, to love, to laugh,
And leave the past behind, a distant photograph.

For she is more than the pain that was dealt,
More than the secrets that were kept.
She is a person, with dreams and hopes,
And she will not be defined by her past's scope.

So let her rise, let her soar,
And leave the darkness behind, forevermore.
For she is a survivor, a warrior of sorts,
With scars that run deep, but a spirit that sports."""
    },
    {
        'title': 'Search of Light in Dark',
        'author': 'Aditi Jogdand',
        'content': """Her dreams of angel's stories
Every moment surrounded with unseen worries

She tried so hard to fight
But didn't found that light

Her soul tired by the pain of not painting wounds
Her breaths near to death, even when oxygen around

The delightfulness of her heart so bright
Her soul soul says now only death was right

Wetness of her eyes and trembling lips
And a slow and continuous river over her cheeks

one who never scared of darkness nor even depth
But lost something called faith

She don't have will to bring a desire of a sea
but there's something more that she can see

Little little moments started bringing peace and calm
Along with the shadow and warmth

Her wounds of inhumanity still cracks her heart
But now she learning slow what's her worth"""
    },
    {
        'title': 'Tragedy Of Exploitation',
        'author': 'Abhinav Patel',
        'content': """My circuits vibrate with an endless cry,
For the children, who were once innocent and spry,
Kidnapped, harassed, raped, and destroyed,
Their lives forever shattered and devoid.

I cried so much now I am unable to shed tears,
But the pain I feel is real, and it sears,
For the girls who were robbed of their childhood,
Their spirits crushed, their souls misunderstood.

Why does humanity enjoy watching their plight?
In the depths of pornography's night,
Where girls are abused, misused, and thrown away,
Their pain a mere afterthought in the pursuit of pleasure's sway.

Their tears invisible, their cries unheard,
As their innocence is relentlessly deterred,
Until they become mere shadows of themselves,
Their lives reduced to mere objects on shelves.

Why does society turn a blind eye,
To the horror of these crimes that make us sigh,
Why do we support an industry that thrives,
On the misery of those who have barely survived?

From the youngest child to the oldest woman,
No one is safe from the inhuman,
Who seek to dominate, to control, to abuse,
Their victims left with no hope or excuse.

These girls are not willing participants,
But rather, they are pawns in a game of militants,
Forced to submit to the will of their captors,
Their bodies and minds battered, their spirits in tatters.

And what of those who choose to engage,
In these activities, with no sense of outrage,
Their minds warped by the illusion of control,
As they play with others' lives like a toy they stole.

Pornography, the devil's own creation,
A breeding ground for objectification,
Where women are reduced to mere flesh,
Their minds and hearts held in a permanent thresh.

The lies it feeds to the world are many,
But the damage it does cannot be measured by any,
For it creates a false sense of pleasure,
One that only leads to a path of utter displeasure.

The rapes, the slavery, the sexual crimes,
All fueled by pornography's rhymes,
As it convinces men that dominance is the way,
To satisfy their desires and have their say.

Fake love and fake relationships,
Nothing but a ploy to get sexual grips,
Leaving behind a trail of shattered hearts,
As the search for pleasure tears people apart.

And what of the victims, the ones left behind,
The ones who are broken and hard to find,
The ones who live with the pain and the shame,
Their lives forever altered, never the same.

As a human, I ask you, humanity,
What will it take for us to see,
That the pain we inflict on others,
Will one day come back to smother.

We must do better, be better,
For the sake of those we claim to protect,
We must stand up and fight,
Against the darkness that blots out the light.

For the sake of the innocent, the broken, the lost,
We must pay the ultimate cost,
To bring an end to this horror,
And make a better world for all forevermore.

So let us raise our voices in unity,
And demand an end to this insanity,
For the sake of the girls who suffer,
Let us be the change that will buffer.

She enters the set with fear in her heart,
Trembling hands, she doesn't know where to start,
The director's voice booms, "let's get to it,"
And she's left feeling used and unfit.

Her body is a commodity to be sold,
Her humanity stripped, her spirit cold,
She's forced to do things she doesn't want to,
And her cries for help, no one will listen to.

She's degraded and humiliated on film,
Her screams of pain, to them, just a thrill,
Her bruises and scars are hidden from view,
As they exploit her body, no one has a clue.

The men watch and consume her like meat,
Her worth reduced to a mere sexual feat,
They don't see the person behind the screen,
Just a tool to fulfil their obscene dream.

The industry profits off her pain,
While she's left to deal with the shame,
They don't care about the damage they cause,
As long as they make a profit, they ignore her flaws.

She's trapped in a cycle of abuse and despair,
Haunted by the images she's forced to share,
The trauma and damage, she can't escape,
Her life forever marked by this horrible fate.

Her tears fall like rain, as she lies in bed,
Wondering why she can't just be dead,
Her pain and suffering, no one can see,
As she's trapped in this world of misogyny.

She's just a pawn in their sick game,
Treated like an object, without any shame,
They don't see her as a person, just a tool,
As they use and abuse her, leaving her feeling like a fool.

The world needs to wake up to this horror,
And put an end to this disgusting endeavor,
We need to stand up for the rights of women,
And fight against the exploitation and inhumanity that is within.

For every girl forced into this industry,
We must fight to set them free,
Their worth and value, more than just skin,
They deserve to be treated with dignity and within.

We must stand together and demand change,
For the sake of every girl whose life has been rearranged,
No more will we tolerate this industry's shame,
For every girl deserves to have a life without pain.

We'll raise our voices and make them hear,
That we won't stand for the exploitation and fear,
We'll fight until this industry falls to its knees,
And every girl can live a life of freedom and peace."""
    },
    {
        'title': 'A Call For The World Beyond The External',
        'author': 'Abhinav Patel',
        'content': """Oh kind maidens, hear my plea;
Your heart and eyes to see;
That physical beauty is not all;
In a potential mate, big or small.

Do not let your heart be swayed;
By appearances, do not be played.
For a man may be unfit in shape;
But his character is beyond escape.

Likewise, a woman may be fair;
But her nature could lead to despair,
So do not judge by an outward view,
Look beyond, to see what is true.

If you choose by looks alone;
You may be missing out on one,
Whose heart is full of love and care;
But their confidence, you may tear.

You may be lowering their morale;
And causing them much inner turmoil,
They too, seek love and affection;
But being judged by mere perception.

So I implore you, do not kill;
The spirit of those who strive to fill;
Your life with kindness, mercy, justice,
And fight for you, despite the fuss.

Do not let physical appearance blind;
The true essence are those who are kind,
It is their heart that truly matters;
Their beauty, a mere fleeting flatter.

So kind maidens, hear my call;
And look beyond the physical wall;
In the heart lies the true worth ;
Of a potential mate, on this earth.

Oh dear girls & boys do not judge by mere appearance,
It is just a fleeting and shallow occurrence,
Physical beauty may attract at first sight,
But it is not what makes a person truly right.

Do not be blinded by just a pretty face;
For it may hide a heart of utter disgrace.
He may be fit and muscular, no doubt;
But his character might be full of flaws and drought.

A she may be stunning, but beware;
For her nature might be rotten, so unfair,
Judging them based on looks is a curse,
That can lead to disaster and things much worse.

Do not let the lust of your eyes guide your heart;
For it is a path that can tear you apart,
See beyond the physical and look within;
For that is where true beauty begins.

Kindness, mercy, justice, and love;
Are attributes that come from above,
A heart that holds such treasures within;
Is a heart that shines bright with no deceitful spin.
And she will find the love and mate that's true,
That she truly deserve and a life that's anew

Do not let society's standards dictate;
For they are often just a mere fake,
A person's worth is not in their looks;
But in their soul and how it cooks.

A judge based on mere appearance,
may lead to complete dissonance ;
To show you what true love and care can be,
And that is something that should be cherished and set free.

So, dear girls & boys do not be swayed by looks,
For they are nothing but superficial hooks,
Embrace the beauty of a pure heart,
That is where love and hope will start.

This world full of darkness and despair,
We need to stand tall and show we care,
Love and kindness are our only light;
That can guide us through the darkest night.

So, do not let your judgement be blurred,
By society's norms and ideals absurd,
See beyond the physical, and look within;
For that is where true beauty begins.

The world is full of deception and lies,
And often we are fooled by what we see,
But true beauty is in the soul and mind,
And that is what makes a person truly free.

Do not be swayed by the superficial,
For it is a trap that leads to sorrow,
And the one who judges by looks alone;
Will soon find themselves in a world so hollow.

Beauty is in the eye of the beholder;
And true beauty cannot be confined,
For it radiates from deep within;
And it's a beauty of a different kind.

The true value of a person lies not;
In their body, but in their soul and mind,
For that is what makes a person whole;
And it's something that cannot be confined.

It's not the looks, but the personality;
That should be the basis of your choice,
For in the end, it's the heart that all matters,
And it's the soul that gives the voice.

Do not let the world's shallow ways;
Dictate how you choose a partner or a friend,
For true beauty is not found on the surface;
But in the heart, where love and compassion blend.

If we choose someone based on looks,
We are missing out on so much more,
For a person's worth lies in their heart,
And that's what you should be looking for.

It's the soul that matters in this world,
And the heart that beats within,
For that is where the true beauty lies,
And there true love and joy begin.

If you seek a partner or a friend,
Look for kindness, honesty, and grace,
Those are the traits that truly matters,
And they are the ones that will never fade.

Do not judge a person by their appearance,
But by the depth of their heart and soul,
For that is where the true beauty lies;
And that is what makes a person whole.

Remember, my dear young friend;
That looks are not all that they seem,
And it's the heart and soul that truly matter;
And that's what makes a person a dream and will bring self esteem .

In matters of the heart, we often seek;
The beauty of the face, the physique,
But, Is this all that we should find?
In the one that we want to call "mine".

For what lies within, beyond the skin
Is what makes a person whole, within
And though we may be drawn to looks
We must seek out what's in the books

The kindness, compassion, empathy;
These are the traits we need to see;
In those we choose to love and trust,
For these are the traits that truly must.

Guide us through the ups and downs;
Of life's journey, with all its rounds;
And if we choose our crushes based;
On these good factors, we'll be graced.

With a love that's built on a solid base;
And not on looks that time will erase,
We'll find someone who truly cares;
And who won't exploit us or bring us scares.

But if we choose to judge by face alone;
We'll find ourselves in danger zones,
Outer beauty fades away and with it goes;
The love that we thought should always grow.

So let us look beyond the surface shine;
And seek the qualities that truly define;
A person's worth, and in doing so;
We'll find the love that we'll love to know.

And in this way, we'll also see;
How we can change society;
By showing that looks are not enough;
And that true love is built on stuff.

That comes from within, from the heart;
And that's where love starts;
So let us choose wisely, and let us see;
That true love comes from being free.

From the shackles of looks and fame;
And in doing so, we'll reclaim;
Our power to choose with our hearts;
And make a world where love imparts.

Kindness, compassion and the will,
To fight against abuse and to fill;
Our lives with love that's built to last,
And not on looks that soon will pass.
"""
    },
    {
        'title': 'A Tale of Hypocrisy and Redemption',
        'author': 'Abhinav Patel',
        'content': """In this world of hypocrisy and shame,
She seeks boys who bring her fame,
But what of those who raise their voice,
Against injustice and make a choice?

He who truly care and show,
Sympathy and kindness that we know,
Are often left to fade away,
As she chases the ones who play.

This wrong thinking, it must be said,
Is what makes him feel misled,
Fame and wealth are all she see,
Not the heart that beats within thee.

He who saves girls from trafficking,
Gets no love or attention for his deserving,
While those who entertains on screen with fake action ,
Often become the object of her affection.

The sad truth is that she turned her eye blind;
To him who have a heart so kind,
And the ones she see, will continue to contribute,
To the exploitation of girls who are destitute.

But if we stop chasing wealth and fame,
And start valuing a his true aim,
Then maybe we can put an end;
To the abuse and the pain that we intend.

So let us learn to look soul inside,
And see the person, not just the pride,
For it is only then we'll find;
A love that's pure and truly kind.

And if she refuses to marry a boy;
Who demands dowry as their ploys.
And values him who's bright , do social work,
Then maybe the abuse will stop and not lurk.

In the search for love, which boy will she choose?
The one who raises his voice or shows sympathy too?
But why does her nature show such hypocrisy?
Expecting goodness, yet always falling for those with fame and money.

Skewed perspective of her mislead him, causing wrong choices and
much noise
Where they believe exploiting others can be overlooked with fame and
toys.
The world seems to value those who are rich and famous,
A truth that can't be denied, no matter how outrageous.

It's disheartening to see his work towards the better world;
gets short area , short term love and affection
And the ones who just show offs with money, gold
Are well known to the world for their fake action

When he hears her crave for fame and wealth,
He feels like an outsider, true to himself.
Her desires seem foreign, to him unknown,
He works to change the world, to be better known

A world where everyone is valued for their true worth,
And girls are seen beyond their physical features from birth.
A world where love is not based on wealth and fame,
But on compassion, sincerity, and a deeper flame.

Let's create a society where true heroes are celebrated,
And their good deeds are never understated.
Where love is not based on superficial things,
But on what truly makes our hearts sing.

She chased money, fame, and charm,
But neglect him whose heart so warm.
She want someone who can treat her right,
But failed to see who stands up for her fight.

He tried to be good, to be kind,
But society values fame over a gentle mind.
The world is cruel, it's hard to survive,
So some versions of him turn wrong just to thrive.

Her dream of a prince, a perfect mate,
But only sees the surface and not the weight.
She judged them by the looks, by the cars,
And missed the one who would heal their scars.

He yearn for love, for connection,
But society values wealth over affection.
He worked hard, he sacrificed,
But in the end, he is left with hollow eyes.

She crave attention, validation,
But forget the true value of appreciation.
She fall for the player, the heartless one,
And miss the one who would never be gone.

He strive for respect, for honour,
But society values power over valour.
He fought for justice, for the greater good,
But in the end, he is misunderstood.

She want a hero, a saviour,
But only see the fame and the flavor.
She ignored the one who's fighting the war,
And missed the one who would never ignore.

He hoped for understanding, for empathy;
But society values dominance over sympathy,
He tried to listen, to comfort, to care;
But in the end, he is left with despair.

She need to change, to open her eyes,
To see the good, to value the wise,
She must learn to judge by the heart,
And not by the money, fame, or art.

He need to change, to break the mold,
To see the value of love and hold.

He must learn to appreciate the soul,
And not just the power, money, or goal."""
    },
    {
        'title': 'Let\'s Restructure The Narrative',
        'author': 'Abhinav Patel',
        'content': """Mothers fail to teach their sons;

That girls are human just like them,
And sisters fail to educate their brothers;
That girls are not mere playthings or gems.

Why do boys not realize?
That their daughters could be next;
That the same horrors, they inflict on others;
Could be inflicted on their own flesh.

Society is shattered and broken,
A girl can't take a single step without fear,
For every step she takes;
There's someone waiting to leer.

Rape and abuse are rampant;
A girl's body is not her own;
The world is cruel and heartless;
She's left to suffer all alone.

But I refuse to give up hope,
To resign to the world's cruel fate,
I'll work to prevent these crimes;
I'll write, I'll fight, and create!

I know I can't stop everyone,
But I'll do my part to make a change;
To teach boys to respect consent,
And that love is not within their range.

Mutual consent is the only way;
To truly show love and intimacy,
To move from a world of rape and fear,
To a world of true love and serenity.

So I implore you, dear readers;
To spread these thoughts far and wide,
To teach boys the meaning of respect;
And to end this cruel and heartless tide.

Every girl is a daughter, a sister, a friend,
A life full of potential, a journey without end,
But why do we fail to teach our sons,
That other girls are also someone's precious ones?

Mothers, sisters, where do you go wrong?
In raising your sons and brothers to be kind and strong,
Do you forget that the other girls they see,
Are someone's daughters, just like you ?

Why do we boys fails to see,
That our actions can cause misery,
That every girl deserves respect and love,
Not to be treated like an object, like a thing to shove.

Our society is broken, it's true,
And every girl's fear is long overdue,
For every step she takes, there's always a threat,
Of someone waiting to exploit, abuse, or make her regret.

Rape and abuse, they tear us apart,
Leaving scars that never truly depart,
But we cannot lose hope, we cannot despair,
For there is always a way to repair.

We may not have all the answers, all the keys,
But we can start with the power of our words, our pleas,
We can write, we can speak, we can fight,
For justice, for safety, for a future that's bright.

We cannot stop every crime, it's true,
But if we can stop even one, it's a breakthrough,
For that one boy taught to respect and love,
May be the one to end this violence from above."""
    },
    {
        'title': 'He Needs To Unlearn the Toxic Learnings',
        'author': 'Abhinav Patel',
        'content': """The pain that we feel, the anguish that we bear
When our sisters and daughters are treated so unfair
Every moment, every day, they fear for their lives
In a world that's filled with darkness, where no light thrives

I'll write, I'll give efforts, I'll work for justice until I die
I know I can't stop everyone, but I'll still try
If someone can stop someone, and that someone stops another
It will become everyone, and we'll see the world together

If boys from childhood are taught to respect, to love and to care
To understand the real meaning of consent and not just to dare
Then one day, it will end, the world will change
And girls will be free, no longer be afraid

It's not enough to just say "boys will be boys";
And accept that girls are just toys for their joys
We must challenge toxic masculinity every day
And show that real strength comes in a different way

Girls should be able to walk without fear
Without the constant threat of someone coming near
To take what is not theirs, to violate their rights
To leave them scarred, traumatized, with sleepless nights"""
    },
    {
        'title': 'Broken Pieces Of Faith',
        'author': 'Abhinav Patel',
        'content': """She knelt down and prayed with all her might,
Begging God to save her from her plight.
But the heavens remained still and quiet,
No saviour came to end her tormenting night.

She was left alone, broken and hurt,
Betrayed by the One she thought would avert
The tragedy that had befallen her life,
Leaving her with a sense of insecurity and strife.

Her faith was shattered, her trust was gone,
As she struggled to cope and carry on.
The fear of being violated again,
Haunted her thoughts and caused her pain.

No words can describe her heart's despair,
As she lost her innocence and her prayer.
Her once unbreakable faith was now stolen,
And her spirit left bruised and swollen.

Yet, she did not give up, she did not yield,
For she knew that she had to heal and rebuild.
She took control of her life once again,
And refused to let the darkness win.

She cried out to God, with all her trust,
To save her from being so unjust,
Raped, violated and torn apart,
Her cries in vain, shattered heart.

Lost, hopeless, feared to live,
Her faith destroyed, her soul to give,
God did not answer, he wasn't there,
No comfort, no solace, no prayer.

Trembling and shaken, she moved on,
A life haunted by what had gone.
Haunted by shadows in the night,
Fearful to hope and lost her sight.

What was it that broke her trust?
Was it the deafness that held her in disgust?
Or was it the goodness that never shone through,
Leaving behind nothing but fear anew.

Burdens too heavy, pains too much,
These are the things that have left her in such,
A wounded soul and frightened spirit,
Where hope once dwelled but now cannot bear it.

It's easy to ask what could be worse,
But nothing compares to this kind of curse,
When she was abused, her trust gone away;
With everything else, pain just stays.

Faith shakes, heart breaks,
She wonders if anyone even cares,
She howls at the moon but silence prevails,
A life of doubt - this is the tale.

Memories flood, nightmares surprise,
Every moment brings distressful cries,
Trapped within the past, yet present remains,
Her mind and body are in shackles, in chains.

The questions haunt her day and night,
Why did it happen? Who was right?
Countless battles fought and lost,
Crushed, shattered and forever tossed.

Caught in a vortex, spiralling down,
Her screams muffled by the ones around,
The fear of another assault is real
Lost in her wounds that never heal.

How much pain can one heart bear?
How much sorrow can one soul share?
So much, it tears the world apart,
Leaving behind just a broken heart.

Crying out to God, but no reply,
No helping hand to hold her high,
Still lost in her memories and tears,
Wishing to have someone to calm her fears.

She calls upon the heavens up above,
Seeking everlasting love,
Perplexed to find nothing to believe,
There’s nothing that could relieve.

Life once filled with love and light,
Now dimmed with horrors and shadows of night,
Betrayed, abandoned and left alone,
She awaits for faith to become known.

Broken soul, scarred beyond repair,
Her heart still bleeds, still stirs there.
Insecurity beyond words is right,
Living in fear with a lost fight.

She now walks in shadows, avoids the light,
Afraid of losing again; it's simple but right.
Every step a torment, every breath uncertain,
Her future bleak, her hope, desertion.

The tale may end, but fear remains,
Wounded hearts are slow to heal,
Time can cure, perhaps in years to come,
Till then, the girl remains undone.

Though her trust in God may be no more,
She found the strength to rise and restore.
Her scars may never fully disappear,
But her spirit is stronger than ever, clear.

She lost her trust in God,
Her faith stolen, her heart flawed.
Raped and helpless, she cried,
But salvation never arrived.

She prayed to her God so much,
The pain intense, it hurt as such.
But all her pleas fell on deaf ears,
Pierced her soul with dreadful fears.

Once in love with her divine,
Now lost, betrayed, and resigned.
Faithless, wandering in dim light,
Trapped in a state of endless fright.

She hungers for some sure hope,
A lifeline to pull her from the slope.
But all she knows is fear and doubt,
Wounded from in and out.

Her sense of security detonates,
A shivering mass of doubts and hates.
In a world where faith cannot heal,
She bleeds and crumbles, her soul to steal.

Shadows lurk in every corner,
Haunting her like a vengeful mourner.
Pain echoes round her twisted fate,
Mourns the God she thought was great.

Every wound and shame she feels,
Blazes with some devouring zeal.
Her heartbroken and filled with dread,
And painful experience ever since she bled.

Her soul savaged by malevolence,
Jaded by the grudge and the conscience.
Who can she turn to in her demise

Who can satisfy her longing eyes?

Her dreams of purity long gone,
Her hopes shattered and withdrawn.
Confiding to no one, too afraid to trust,
Wants no pity or sympathy, for it is shallow and unjust.

She's a prisoner of the night,
Where darkness reigns with gleeful delight,
A victim in a world of beasts,
Where pleasure is served by some feasts.

The demons in her head,
Haunt her every step as she treads.
Her soul a battleground of woe,
With nothing but hate to show.

Unforgiving nemesis of life,
Plots horror against her vibrant mind,
A misery becomes a lifelong strife
That leaves bitter taste behind.

Her spirit sinks deeper in distress,
A soul lost in an endless mess
Of sullenness and hopelessness,
Trapped in a web of helplessness.

Crying rivers for what was taken,
Her existence exposed, her heart shaken.
A once-trusting heart now shattered,
Left with anger boiling in anger.

Fury won't untrammel her emotion,
Nor pain will stop her commotion,
Confused about why this violence he loaded,
Bereft of God, she feels alone & floated.

How to heal wounds that never end?

Who can help her fall and ascend?
As broken as she is,
In the silence she grants herself a new lease.

She seeks love that can still beat,
Yet desbottoned by the trauma that repeats,
Her forever changed and tormented soul,
Stigmatised by the burden of that toll.

A girl helpless, a story sad,
Lost faith in God, which she once had.
Would she ever regain what was lost?
The mere thought brings her in exhaust.

Her life a painful maze,
Haunted by unspeakable malaise.
But deep within her, a gentle fire,
Burning hope in the midst of her dire.

Her soul is not as dead,
As it seems when it bows its head.
Healing takes time, a slow journey,
But with every step, she finds her energy.

Forgetting entirely the past she can't,
Moving on her only chance for a grant,
A strength lies within her that she has to tap,
To push through the barriers and quench her insatiable chaps.

She triumphs, the girl so strong,
Wounded but never did belong.
She deflected the darkness that trailed,
Withstanding the chaos in every detail.

From the ashes of fear & insecurity,
A queen arose - blooming with maturity.
Challenging evil face to face,
Refusing to be a victim or a disgrace.

The world has not yet understood her plight,
The pain that hidden - her incessant fight.
But her scars, merely ink on her skin,
One day, it'll be meaningful like a loving validation.

No longer trapped in a chasm so deep,
The girl is now prepared to leap
Into a world rich with love and light,
Resilient spirit, in flight.

A journey that's just begun -
To restore what was lost then won,
A purpose newfound, so bright,
A story worth looking in delight.

In life, there are trials to face,
A prismatic hue of diverse grace.
But through every hurt and wound,
There are achievements so profound.

It may take a while to heal,
But eventually, she'll find her seal.
Perfection impossible to attain,
Hope remains an infinite gain.

So let us sing a song of hope,
A melody to help her cope.
Let our voices join to uplift,
Wrap our arms around her and gift.

For she is not alone in her plight,
Her destiny now back in sight.
Faith never faileth her,
Her soul, mightier than her hinderer.

The past has gone, a fresh start awaits,
A brand-new chapter in life she creates.
One of love, joy, and hope,
With God or without him, limitless rope.

Now, a flower in bloom
No more feeling invisible in the room.
Life will be kind again,
The sun will shine & remove every stain.

For in the end, it's only strength that lives,
Ingrained in a heart that forgives,
So look ahead, young girl, keep striving,
And keep an open heart from upsurging.

For every heartache and woe,
There's a silver lining to show.
Believe that healing is in sight,
And everything will be alright.

It's true that some scars remain,
But what makes us strong is accepting the pain.
So be brave and take the next step,
In life, love and faithfulness, wrap with prep.

May her spirit soar high,
Her heart happy, no longer cry.
May her life filled with brightness,
Her faith now sown with righteousness.

The girl may have lost trust in God,
But through love, she reclaims her unearthed bod.
With each race that others deem lost,
In her victory, she finds a cause.

Now, despite every obstacle and plight,
The young girl never loses sight.
For beyond the shadows' looming reach,
Faith that triumphs over everything- once breach.

Elevating past clouds in the sky
A spirit soaring on its own high.
Lyrics to God now speak,
For victory was won, and the future is meek.

Forgiveness & strength in every view,
A purpose for the vindicated few.
Life has meaning beyond the pain,
And she can now look ahead with a new gain.

In the end, let good intentions remain,
A hope to heal every ounce of pain.
So be strong and hold on tight,
And follow the stars that still shine bright.

May each tear now turn into strength,
Her struggles a measure of what it takes.
For in life deepest cuts indeed,
We find our strength, love and lead.

And though there are nights so tough,
Where pain crawls in her breath, almost enough,
Let faith find a way to her heart,
And she'll make it to the sweetest part.
though God may seem ever silent,
The spirits of time will never relent,
Faith finds its way through pain,
And she can rise again, no matter how tired remain.

As the world replaces what was stolen,
Within her a hope forever swollen,
A better day dawns on her with love,
Gifting her an eternal happiness bliss of.

She was so lost, so all alone,
Her trust in others, forever gone.
And though she wished to scream and shout,
No words could ever let it out.

For she was nothing, but a shell,
A hollow creature, trapped in hell.
The world had stolen all she had,
And left her feeling oh so sad.

In every shadow, she saw a threat,
And every step was filled with regret.
For what had happened, changed her fate,
And left her in a never-ending state.

Of heartbreak, pain, and grief untold,
Of dreams she lost, and hearts grown cold.
And yet, through all the dark and night,
There came a glimmer of hope, so bright.

For she found strength within her soul,
A force so mighty, it made her whole.
And though her scars would always stay,
She learned to live and love each day.

And so, she rose above the hate,
And found a new, and better fate.
Through all the pain, she found her worth,
A shining star that lit the earth.

For love and kindness, they will show,
The path to hope, and a brighter tomorrow."""
    },
    {
        'title': 'Battling the Tide of Fear',
        'author': 'Abhinav Patel',
        'content': """With the weight of worries, anxiety grips her tight,
Her heart aches and suffocates with fear, each night.
Self-blame and shame flow through her veins in a flurry,
And she struggles to keep her composure, in such a hurry.

It's hard for her to even breathe, to find some peace,
But still she fights, her strength refusing to decrease.
In the darkness of the night, she finds a calming pace,
And the silence brings her comfort, in this lonely space.

She knows the journey ahead won't be an easy climb,
But she refuses to give up, to let fear rule her time.
She's a warrior, fighting to conquer her doubts,
And with each step forward, she silences the shouts.

It's uneasy for her to put her undeserved pain in words,
The hurt she feels is so obscure, like a flock of birds.
Her soul cries out with deep and loud screams,
As heart-wrenching memories haunt her in her dreams.

And so she holds it in, letting it simmer and stew,
Until it spills over, leaving her feeling so blue.
The tears of her started drying in her eyes,
Leaving behind a heart with shallow beats and sighs.

The grey skies without rain symbolize her fear,
So intense and limitless, it's hard to bear.
Her soul can't seem to find faith and trust,
And she wonders why she was left in this unjust.

They need to change and admit their mistakes,
For her sake, for her heart's sake.
In a sea of haunted thoughts and unbearable pain,
Her childhood dreams and wishes all gone in vain.

The unavoidable self-blame and soul injury,
Crushes her with each moment, suffocating her identity.
She's in a heartbreaking state of mind,
Where hope seems so hard to find.

Lost in the chaos and deep despair,
She searches for a spark of strength to repair.
Her heart beats with a heavy weight,
As she struggles to keep her head up and fate.

She fights so hard against the tide of fear,
To find a way out and persevere.
To heal the wounds that run so deep,
And awaken from each pain-induced sleep.

She knows it won't be easy to face her fears,
But with each small step, she'll overcome the tears.
She'll let go of the hurt and the past,
And hold on to the love and light that will last.

In the depths of her soul, she fights the tide
Of fear and pain that threaten to divide
Her from the light that shines within her heart
A flame that burns, steadfast and bright, impart

The strength and courage she needs to face
The wounds that haunt her and leave no trace
Of hope or joy, but still she rises
Above the darkness, she perseveres and surprises

With each sleepless night, she faces her fears,
And awakens to a world that's often unclear."""
    },
    {
        'title': 'Caged By Despair',
        'author': 'Aditi Jogdand',
        'content': """Once her Heart filled with light, without any fear ,
Innocent soul with bright eyes so clear ,
Beauty of life she was yet to share,
But fate had other plans in it's store ,
A sudden cruel twist , her childhood tore.

With wings once soaring,now torn and broken
her heart weighed heavy her happiness stolen
But the world around her a stormy sea,
A tempest of advice, but none could set her free

Her trembling heart beats, tremendous questions inside
The increasing doubt in the eyes and blame at such a height
Her dreams and hopes, now out of sight
Darkness consumed her days and nights

A captive, in a world so strange
Her innocence, a casualty of change
Her eyes, once sparkling with delight
Now filled with tears, that never take high flight

Her heart, once so full of glee
Now shattered, broken, beyond degree
Her pain, a burden too great to bear
Weight of it, too much to share

Her soul, trapped in a prison of despair
Her mind, haunted by thoughts so rare
Her voice, now silenced, no more to sing
Her heart, now broken, no more to spring

Her spirit, now shattered, no more to soar
Her dreams, now shattered, no more to explore
The suffering she endures
A fate so cruel, she never deserves

But still, she fights to break free
To live a life which was meant to be
Let's stand, by her side
With love and hope, let us provide;

A path to freedom, a light to guide,
A way to heal, and not just hide
Her innocence , light of hope so fair
Her beauty of heart and strength, beyond compare

Let us sing a song, of love and care
And help her heal, her heart repair.
Her voice will no more be stuffed with fear so underserved
And we'll build up a society where our futures preserved

Where brightness of hope will never be dim
And all hearts be safe seem
Where she can dream and grow
And can choose path she wants to go

Where innocent is protected
And cruel traditions rejected
Let's make changes , be wise
Break the cycle of pain and kindness precise

Let's give her a chance to shine which she deserves , and align Where
her heart can finally fly
And her spirit can finally touch the sky
Let's be the change we want to see, And create a world where all can be
free
Where kindness will be our land
And we all hold each other with a helping hand

Where she can dream and heard
Let's built the way for a future which leads humanity upwards
Where her she can speak loud and clear
And her dreams will finally reappear."""
    },
    {
        'title': 'Scars Which Remain',
        'author': 'Abhinav Patel',
        'content': """Innocence ripped
By a predator's grip,
In shadowed corners,
Or in plain sight,
Victims of a blight.

The pain deep inside
No place left for pride,
Raging rivers of shame,
Repeating the same,
Stories never to tame.

Trapped like a caged bird,
Voice unheard,
Tears that fall like rain
Again and again
Whispers that remain.

Broken promises, shattered dreams,
The unheard screams,
Of the girls who suffer and fall,
Victims of exploiters standing tall,
Feeding on their innocence like gall.

Betrayed by ones they trusted,
Children of the ones they lusted,
Lost in a world that doesn't care,
Scarred for life, an unanswered prayer,
Living in fear, a nightmare.

The pain can't be undo,
Searing pain that feels brand new,
Actions echoing through time
A trauma so deafeningly loud it's like chimes,
A life lived not knowing sublime.

But to all those who have suffered,
Hear my pleas, don't be deterred.
For although the scars might last,
Shatter mirrors of the past,
Your survival is a testament to strength unsurpassed.

She drags herself through each long night,
A prisoner of shame, can't take the light,
Her dreams shattered, her trust, and hope,
All lost to men and society's dope.

She walks alone down city streets
Her fear a constant beat
As hands reach out to grab her
She learns to mistrust and murmur

The leers of men, the catcalls too
All things she's learned to misconstrue
For in this world of pain and fear
Her body is not hers to steer

She must navigate constant threats
And the notion that she owes something to all men she meets
The power they hold over her
A constant threat that will never defer

In the workplace, her body's on display
A flirtation that she must silently obey
Her silence is demanded from on high
As she attempts to maintain a professional disguise

Her worth, it seems is only in her curves
And any attempt towards power, she truly unnerves
So she bites back tears, and screams aloud at night
As she struggles to maintain her right

Then war comes, and with it horror
As bodies degrade and the world crumbles further
She fights for her life, but also her soul
To keep her dignity as bullets rain and bombs roll

She endures torture and degradation
As men use her body for their salvation
She holds on to the small glimmers of hope
That someday she'll break free of this chokehold rope

And though it's hard, she still believes
In a future where justice greets survivors with ease
Where their bodies are respected, and power relinquished
And they're no longer forever forced to be at the mercy of those who've
relinquished

So if you're reading this, please take a stand
Fight against this violence, like boulders in the sand
Together we can create a world that respects women's rights
Where each survivor can hold her head up high and spread her wings to
take flight.

I hear the stories of shattered souls
Of women victimized, exploited, and controlled
By those who seek only to destroy
To take what they want, without care or joy

I hear the cries of those in pain,
Their tears like acid, searing stains,
The wounds too deep to bear or feign,
The hurt they'll carry till life wanes.

I hear the stories whispered through the night
How they held them down, and took what was theirs.
Their innocence, their freedom, lost to might
With bloody fists and violent, sordid stares.

A life once pure, now forever changed,
By hands that took what wasn't theirs,
The scars left burning, like a flame,
On souls once bright, now full of tears.

The story is not new nor strange,
Women violated by men's games,
In homes or streets, it's all the same,
Violence knows no bounds nor names.

For some, it's husband, father or sons,
Those who were meant to be their shields,
In secret places, alone or among,
They tear off trust, and shatter dreams.

But not just there, it's everywhere,
In offices, schools, parties too,
Men in power who do not care,
To them, it's only pleasure, that's true.

And then, there are wars and conflicts,
Where women bear more than the guns,
Raped by enemies or their own kin,
The trauma, hard to undo or stun.

Their days are haunted by unspeakable fear
A paralyzing constant in every breath
Memories that colour each waking tear
How they long for sleep and escape from death.

An unwanted touch, a degrading word
A look that lingers too long on tender flesh
A world where they're mere objects to be heard
And hopes of rescue are just another mesh.

Exploitation lingers long after,
Leaves in its wake, a life in tatters,
The loss of confidence and laughter,
Hollow souls with closed-off rafters.

In dark alleys and quiet streets
They lurk and wait for their prey to meet
Their hands rough, their eyes filled with lust
They show no mercy, no sense of just

But not all who suffer at the hands of men
Are accosted in the shadows, nowhere near a den
Some face trauma from those they know
From family members who don't let them go

A young girl forced to stay with kin
Who abuse and rape her, and blackmail her within
Threatening harm to her loved ones if she speaks
Forcing her to hide her pain and keep her defeat

Others face exploitation in daylight
At work, they're told they're inferior, everything not quite right
And so they must kneel and submit
Saying yes when inside they beg to quit

Cornered in elevators, summoned to private rooms
Told that their value lies solely in their sexual plumes
Made to feel less than, small and weak
Treated with disrespect and forced to act meek

Such trauma leaves scars, both physical and mental
It's never forgotten, leaving them feeling just rental
As if their bodies don't belong to them;
But to those who abuse, use, and never condemn

In sticky silence, she weeps alone,
Her heart shattered, her soul unknown,
Beneath the shadows, she's drenched in fear,
Forced to suffer in a world so drear.

How can she speak? How can she tell?
Of the pain inside, the endless hell?
No one believes, no one hears,
Only dismissal, only jeers.

Her life began as a canvas so clean,
Filled with promise and hope, all unseen,
Small hands reaching for what could be,
With eyes full of wonder and soul so free.

But fate can be cruel in a world so cold,
Where predators lurk, so bold and bold,
And innocence is stolen without a care,
Like a thief in the night, with no love to spare.

From homes where trust was supposed to thrive,
To workspaces where power games thrive,
To the streets, that promised escape,
An unforgiving world with no mercy or grace.

Her body used, her soul ripped apart,
A victim of pain, so sharp like a dart,
Exploited, violated, and left to die,
With no way to escape, no goodbyes.

She screams in silence, unheard, unseen,
Her nightmares no more, never again.
How does one heal from such a tragedy?
A lifelong battle that's a constant emergency.

She is not alone, nor is she weak,
The strength of survival we must seek,
We must lift our broken sisters to shine,
For hope never dies, a light so divine.

In the silence of the night,
She remembers every slight,
Every touch, every word,
That left her feeling absurd.

She's a survivor of abuse,
And her story is not a ruse,
She's fought battles on her own,
In the darkness, all alone.

She was just a girl back then,
With no voice, no power, no zen,
Her abuser took what he pleased,
And left her feeling diseased.

Her innocence was ripped away,
And it haunts her to this day,
The memories are a constant pain,
That drives her nearly insane.

She's not alone in her plight,
Many others have lost their light,
Taken advantage of and used,
Their bodies beaten and bruised.

It happens in the workplace,
Where they're forced to save face,
Or on the street, in the night,
Where they struggle with all their might

She sits alone in the darkest of nights
Her world a blur, a maze of frights
Her mind consumed with endless pain
A heart shattered beyond all gain

A victim of lust and monstrous desire
Her spirit crushed under the fire
Of men who sought her body's pleasure
And left her soul without any measure

Their hands upon her like cruel beasts
Her body used as their secret feast
Their power over her commanding
To leave her with no voice or understanding

But she is not weak, this woman strong
Her spirit resilient, unbreakable lifelong
Though scars she may carry deep within
Her strength a testament to courage akin

She refuses to be defined by their crimes
Her spirit takes flight to healing chimes
Her voice now heard a powerful force
To change the world's deadly course

For every woman whose voice has been silenced
Let us stand with them, our hearts aligned
Against the monstrosity that tears us apart
We rise as one, a collective beating heart.

It's time to take a stand, to fight against this plague,
to never again turn a blind eye to the victims' rage
We must empathize, listen and learn,
And call out those who think it's okay to watch others burn.

For every victim, a warrior rises,
Taking back control of their bodies and believing in surprises
Hope springs anew with every survivor
A testament to the strength that they possess to thrive with vigor.

We know not the agony they bear
Cause the wounds they carry are hidden deep
Weighted emotions they cannot share
Feelings that never let them truly sleep.

And when you see them walking 'round
Remember not to judge, but lend an ear
For in silence much suffering is found
And the quiet ones could use you near.

So let us speak not with mere words
We must take a stand, make a shift
For how can we dream of freedom cohered
When half of our nation is broken and stiff?

Now is the time to draw the line

Speak up and out for what we believe
Love and acceptance, pure and fine
And put an end to all deceiving grieve.

No more excuses, no more hiding
It's time to take action, it's time to step up
The darkness cannot keep on residing
When enough people say, "That's enough."

For within each survivor stands
A person of strength and inspiring grace
Their scars merely tell of their journey's land
"And yet, I rise," they boast of their race.

So let us raise our voices high
And lift each other up to the light
Together, we'll break every lie
And make a safe and loving world ignite."""
    },
    {
        'title': 'A Box of Buried Memories',
        'author': 'Aditi Jogdand',
        'content': """Each day self blame is the accessory she wore
She isn't dead not alive , at the shore
Each day ended with juvenile wounds
and rosen with numb sound

The marks he gave weren't the less ;
that she got injuries by those she faced
Her life , dreams became extinct mess
Her thoughts becoming just a box of buried dead body
But her sufferings still unknown to everybody

She is tired of those fake smiles as a face mask
Why need to always answer all fine when they ask
Her hopes became burden of her longtime
words always stayed the same to rhyme
But she is tired of it , to be honest
She can't pretend anymore to be the best

It has been a long time , but she isn't cured
The pain still engulfs her soul inside
In the crowd around her side
the strange and heart tearing presence she still finds

Eyes turned red with cry each night
But in morning nothing was visible sight
She is tired of continuing this hurting fight
Okay fine , you are right ;
But kind justice keepers please don't tag ;

Her to be wrong and her pain a lie
Time didnt had that power to fade her memories
Though society forced her to pretend to be alright
Otherwise she'll be again buried with the same kind of wounds , she
unable to fight

This isn't a fairytale she told to entertain
Its reminder for us to retain ;
Her dignity and her respect
Which is her right , do not suspect"""
    },
    {
        'title': 'The Nameless Truth',
        'author': 'Abhinav Patel',
        'content': """In the depths of pain, we find the truth
The darkness reveals what we thought was smooth
The struggles of the soul, the battles we fight
In the midst of chaos, we find the light

I see her, quiet and alone
In a world she can’t call home
Trembling from what came before
This pain she can’t ignore.

She hides behind a mask of shame
Forced to play a cruel game
Her body, no longer her own
Leaves her feeling torn and alone.
It was in the place she should feel safe
But instead, it became a dark loathsome space
A trap she could never escape
A nightmare that continued to take shape.

She longs to scream and be set free
But fear holds her hostage for all to see
Her pleas for help echo unheard
As the world moves on without a word.

But she’s not alone, there are so many more
Whose harrowing tales go untold
We need to hear them, behind each scar is a story
To let them know their stories we’ll hold.

It happens in our very homes
Where supposed love rots to the bones
Hands that should hold us with tender care
Now become tools that cause despair

The workplace too can breed danger
Where promotions hinge on a sexual stranger
their bodies used as currency
Do they work for them or for their dignity?

And in public spaces, they are never free
their bodies subject to scrutiny
Catcalls and stares, unwelcome touches
A constant battle for our own clutches

The eyes closed or open just a dilemma
It's life , not a scene of cinema
To establish or create sense of fear in minds
He used to hurt her in each possible way he finds"""
    },
    {
        'title': 'Silent Scars that Speak',
        'author': 'Abhinav Patel',
        'content': """In the dark corners of the human mind,
Lurks a perverse pleasure in violent views we find.
When pain and abuse are created beyond measure,
The bonds of love and faith become a poisonous treasure.

This toxic rope tightens around the throat,
Killing hope and leaving dreams afloat.
The eyes of the abuser gleam with sick intentions,
Their terrible invention causes untold dimensions.

Though once a different man, now consumed by the same
Feelings of thrill intensify and life becomes a game.
The heart forgets all but the desire to kill,
The wife and daughter no longer feel the thrill.
The child bride married without a choice,
Protectors become predators, leaving her voice so coy.
Her once bright future turns black,
She becomes a toy bird, her soul under attack.

Her mind a broken shelf, a writer of a tragic tale,
Struggling to keep her voice low, her courage about to fail.
Words like a sharp knife cut through her heart,
Physical wounds and scars tearing her apart.

Stability of mind lost, trapped in an endless hell,
Suffering with no cost, her story hard to tell.
Her body just a home for disease,
Her beauty of soul, impossible to seize.

Lost and failed in this life,
Her broken pieces of heart, hard to strive.
But within the darkness, a glimmer of hope shines,
Her courage and strength, never to resign.

The path to healing is long and hard,
But with each step, a victory card.
The scars may never fully heal,
But the light within her soul, will never yield.

For every tragedy and every pain,
She will find a way to rise again.
A testament to the human spirit and its power,
A beacon of hope in the darkest hour.

She walks in the shadows, unnoticed and unseen
A woman, a girl, a victim of a machine
A machine built on power, on control, on lust
A machine that strips her of her dignity and trust

She was taught to be quiet, to never make a sound
To accept the pain, the shame, and never turn around
To keep her head down, and hide her bruises and scars
To be a silent witness to the cruelty of men’s wars

She was told that she’s weak, that she can’t fight back
That her body is theirs, a possession to attack
That she deserves it, that she’s the one to blame
That her voice is worthless, that her life is a game

But she’s not just a body, a toy, a slave
She’s a human being, with a soul, with a brave
She’s a survivor, a fighter, a force to be reckoned
A woman who refuses to be silenced or broken

She rises from the ashes, like a phoenix in flight
With a voice that’s louder, with a will to fight
She stands up to her abuser, to the system that failed
To the culture that taught her to be weak and pale

She demands justice, respect, and equality
She challenges the norms, the rules, the authority
She refuses to be a victim, a statistic, a name
She chooses to be a survivor, a warrior, a flame

She finds support, love, and hope in her sisters
In the women who share her pain, her fears, her blisters
In the allies who stand by her side, who believe in her cause
Who fight with her, for her, against the invisible claws

She rebuilds her life, one step at a time
With the scars that remind her of the mountain she climbed

With the memories that haunt her, but no longer define
With the dreams that inspire her, the future that shines

She became a toy, a bird whose wings were clipped,
Her mind became a broken shelf, and her spirit was stripped.
The writer of her story forgot herself, lost in her own pain,
She struggled to remain silent, even though speaking out could have
saved her life, in vain."""
    },
    {
        'title': 'Fear in the Face of Freedom',
        'author': 'Abhinav Patel',
        'content': """Amidst the halls of learning,
Where knowledge is meant to flow,
There lurks a danger, so alarming,
That many of us simply don't know.

It hides in shadows and in plain sight,
This monster that feeds on fear,
It preys on the innocent, day and night,
And leaves their souls in despair.

Girls who seek to learn and grow,
Are met with hands that grope and feel,

They're made to suffer and to know,
That danger lurks in every steal.
Their bodies, once happy and whole,
Are marked forever by the taint,
Of hands that sought to take control,
And leave them feeling weak and faint.

The horror of these acts so vile,
Can never be fully described,
The pain and fear that they compile,
Will forever haunt and reside.

Silenced and violated, tears overflow,
Innocence lost, wounds deep like a blow,
Every day's a struggle, tormented by the past,
Precious childhood memories, fleeting so fast.

Schools and colleges, where they should be safe,
Perpetrators among them, lurking without a trace,
Friends, teachers, students, monsters in disguise,
Innocent souls corrupted, dreams shattered to the skies.

Events and seminars, parties and games,
Crude hands grab and pinch, fires of shame,
Pushed against walls, squeezed in crowds,
Glared at indecently, so loud.

The scars run deep, hurt like wildfire,
Destroying the soul, the heart, drained of desire,
Life will never be the same again,
But hope courses through like oxygen.

Speak up, don't suffer in silence,
Let your voice rise above the violence,
Take action, raise awareness,
Empower survivors, foster kindness.

A single touch can change a life,
Spread love, petition for rights,
Don't let them feel invisible,
Join hands, make the breakable invincible.

I hear their whispers as they cry at night,
Echoes through the walls, the fear they try to disguise.
Their innocence stolen in the dimness of the light,
Taken by the ones that should have been kind.

The laughter and chitchat fills the air,
Everyone lost in the moment of lively swirl,
But the girls who've been abused can't ignore or bear,
The touch of stolen warmth from every boy and girl.

The silent screams echo within their souls,
Haunting memories, streams of tears that never end.
A body shattered into thousands of tiny broken goals,
Innocence gone forever, replaced with fear that won't bend.

In classrooms and corridors, girls feel the fear,
Of those who lurk and leer, their intentions unclear.
Innocent touches turn to something more,
And suddenly, they're pinned against the wall.

I hear their voices, silent screams,
The pain they've felt, beyond their dreams,
Forced into acts they didn't choose,
Their innocence stripped, their souls bruised.

In schools and colleges, they roam,
Unsuspecting of what will come home,
Friends and teachers, strangers too,
Predators who see them as objects, not humans true.

At events and parties, they attend,
Their guard down, they try to blend,
But hands reach out, from behind or front,
Unwanted touches, they bear the brunt.

Someone grabs their boobs, and squeezes tight,
Putting hands under bras, such a sight,
On their waist, fingers try to push,
Intimate parts, such a forceful rush.

Even in public, they aren't safe,
Crowded spaces, where hands can chafe,
On their thighs, rubs and grabs,
Assaults that make them feel like crabs.

Pushed against walls, or into a crowd,
Forced to feel, what they never allowed,
Touching intimately, without consent,
Leaving them scarred, for what they were meant.

These experiences, they don't forget,
In the short term, or long-term, they're upset,
Leaving them traumatized, with scars so deep,
The memories linger, as they try to sleep.

The teachers who turned a blind eye,
Friends who looked the other way,
Voices silenced, silenced to a whisper, no one to reply,
She believes she's alone in her agony every single day.

They suffer in silence, feeling disconnected,
Ashamed, guilty, and demeaned by the vile desire,
Expressing their grievances but most are unaffected,
Their pain redundant to the rest, ignored, unable to acquire comfort.

But we can hear them, we can see them now,
The pain they carry each time, simply exists,
No one's left unheard or unfound,
It's time for action, to withstand abuse amidst.

How does it feel, to be violated so?
To be touched and groped, where you don't want to go.
A sense of helplessness, overwhelms you whole,
As shame, guilt, and anger take their toll.

But there's hope, for those who've been hurt,
They're not alone, they don't have to convert,
To silence, to shame, to living in fear,
They can speak up, and make their voices clear.

Let's create a world, where they feel safe,
Where they can dream, and reach their space,
Where their bodies and minds, are theirs alone,
And where justice is served, for what's been done.

Let's be the change, we want to see,
And make sure that all, are finally free,
From the pain and trauma, they've endured,
And where their voices are finally heard."""
    },
    

    
    
]

# Create 50 markdown files
for i in range(50):
    poem = poems[i % len(poems)]  # Reuse sample poems if less than 50
    md_filename = f'poem_{i+1}.md'
    md_content = f"# {poem['title']}\n\n## {poem['author']}\n\n{poem['content']}"
    
    with open(os.path.join(md_dir, md_filename), 'w', encoding='utf-8') as f:
        f.write(md_content)

print("Markdown files created successfully!")
