import marimo

__generated_with = "0.10.14"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md("""# A visual introduction to Active Inference <br> or how to find the cookies in a dark room?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This tutorial is heavily based on the [Tutorial 1: Active inference from scratch](https://pymdp-rtd.readthedocs.io/en/latest/notebooks/active_inference_from_scratch.html) from Conor Heins and the knowledge from the [Active Inference book (2022)](https://direct.mit.edu/books/oa-monograph/5299/Active-InferenceThe-Free-Energy-Principle-in-Mind). 

        The idea was to add more graphics to make it more intuitive.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "room-image.png"),
        width="60%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Have you ever woken up in the middle of the night, craving a midnight snack? You remember leaving those delicious cookies on your desk, but there's one small problem - the room is pitch dark. We've all been there!

        What happens next is fascinating: without even thinking about it, your brain executes a remarkable navigation strategy. You carefully stretch out your hands and start moving through the darkness. Maybe you brush against something cold and metallic - ah, that's the radiator by the door. Your feet feel the soft carpet in the middle of the room, giving you another clue about your location. With growing confidence about where you are, you take two careful steps forward until your hands find the familiar wooden surface of your desk. Success! A moment later, you're enjoying those cookies you've been craving.

        This everyday experience perfectly illustrates how our brains solve complex problems through a combination of prediction, action, and sensory feedback. In this tutorial, we'll explore this process through the lens of Active Inference, using this relatable scenario to understand how our brains navigate uncertainty to achieve our goals.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Active Inference Loop""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Now let's explore how this seemingly intuitive process actually works. While finding cookies in the dark might seem simple, there's some fascinating complexity behind it that we can simulate and understand.

        To break this down, let's first identify the key elements at play. At its core, we have two main components that interact with each other:
        1. The person (that's us!) trying to navigate
        2. The room with all its objects and spaces

        We can think about this more broadly: in any similar situation, we'll always have an active agent (like us) interacting with an environment (like the room). This framework applies not just to our cookie quest, but to many real-world scenarios where an agent needs to navigate and interact with its surroundings.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "env-agent.jpg"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Now lets take a closer look at these two elements.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### 1. The agent - us as person""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Let's take a closer look at our agent, ourselves in this case. To understand how we navigate in the dark, we can break down our capabilities into three key components:

        #### 1.1. Observation/Perception States
        These are our sensory inputs - in this case, what we can touch and feel. When we make contact with objects in the room, our brain receives this information as observations. For simplicity, we'll assume we can immediately identify objects by touch (like knowing it's a chair as soon as we feel it).

        #### 1.2. Brain Processing
        Our brain acts as the command center, processing all incoming sensory information. Like a sophisticated computer, it takes these observations and performs complex calculations to figure out two crucial things: where we are in the room, and what we should do next to reach those cookies. We'll represent these mental calculations in our upcoming diagrams as processing units within the brain.

        #### 1.3. Action Generation
        Finally, based on our brain's calculations, we take action. In our cookie quest, these actions are simple movements: going left, right, up, or down. Each action changes our position in the room, which in turn leads to new observations, creating a continuous cycle of perception and action.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "loop-agent.png"),
        width="40%",
        style={"display": "block", "margin": "0 auto"}  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### 2. The enviornment - the world""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Now, looking at our environment - the room itself - we can identify two interconnected aspects:
        1. The objects we can touch (like the chair, desk, or bed)
        2. The positions in the room where these objects are located (room position)

        These aspects are naturally linked - each object has its fixed position, and each position contains a specific object. This relationship will be crucial for understanding how we navigate the space.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "loop-environment.jpg"),
        width="40%",
        style={"display": "block", "margin": "0 auto"}  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### 3. Closing the loop""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "loop-environment-agent.png"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        We have gathered all necessary variables for the moment. Now let's try to arrange them in a meaningful way.

        Based on our current room position, we will have certain objects around us. While we can't directly see our room position in the dark, we can touch the objects. These touches generate our observations, which are then sent to our brain for processing. Our brain performs calculations based on these inputs and decides on an action - in our case, simple movements through the room. Each movement changes our room position, which leads to new objects within reach, generating new observations, and the cycle continues. The loop is closed.

        This elegant cycle of perception, processing, and action is the foundation of active inference. Everything we'll explore from here builds upon this basic loop, either refining specific parts or scaling it to more complex scenarios. But you've already grasped the fundamental way our brains navigate uncertainty - whether we're searching for midnight snacks or solving complex problems!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""# Active Inference Implementation as Code""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        In this tutorial, we'll break down our cookie-finding adventure into two key challenges that our brain solves:

        1. **Understanding Where We Are (Variational Free Energy)**
           First, we'll explore how our brain figures out our location using touch-based observations. This process, known as minimizing Variational Free Energy (VFE), is like solving a puzzle where each touch gives us a new clue about our position.

        2. **Deciding How to Move (Expected Free Energy)**
           Then, we'll look at how our brain plans the best path to the cookies. This involves calculating Expected Free Energy (EFE) to choose actions that will most likely lead us to our goal while avoiding bumping into furniture!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "overview-VFE-EFE.png"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### 0. Environment""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Let's start by translating our room navigation problem into a format that a computer can understand. To do this, we need to convert our intuitive understanding into structured data—specifically, numbers and tables that can be processed mathematically.

        To begin, we'll simplify the layout of our room into a more abstract representation. Imagine drawing a floor plan and dividing the space into a 3x3 grid. Each cell in this grid will be assigned an index, allowing us to systematically represent our environment and the objects within it.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "room-plan.png"),
        width="20%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell
def _():
    from pymdp import utils
    import itertools

    """ Create  the grid locations in the form of a list of (Y, X) tuples -- HINT: use itertools """
    grid_locations = list(itertools.product(range(3), repeat = 2))
    print(grid_locations)
    return grid_locations, itertools, utils


@app.cell
def _(grid_locations, plot_grid):
    plot_grid(grid_locations)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Now let's plot our objects from the room on the plan. This gives us the following table, with each of the nine room positions having each one belonging object.""")
    return


@app.cell(hide_code=True)
def _(mo):
    room_plan_obj = mo.image(
        src=str(mo.notebook_location() / "public" / "room-plan-objects.png"),
        width="20%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    room_plan_obj
    # mo.carousel([room_plan_obj, "hi"
    # ]).style(width="500px", height="500px")
    return (room_plan_obj,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Great! We have set up the room plan representing our environment""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## 1. Understanding where we are - Variational Free Energy (VFE)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Our treasure map - "A Matrix"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Let's explore one of the most fascinating aspects of our cookie quest: how our brain figures out where we are in the dark room. 

        Imagine you're playing detective, but instead of visual clues, you only have touch. When your hand brushes against objects—the cold metal of a trash bin, the soft texture of a carpet, or the smooth surface of a table—your brain uses these tactile clues to deduce your location. This process is remarkably sophisticated, yet we do it almost effortlessly.

        But how does our brain make sense of these touch-based clues? Think of it like having an internal map or cheat sheet that we've developed over time. Every time we've spent in the room with the lights on, our brain has been quietly learning and creating associations: "When I touch the carpet, I must be in the middle of the room," or "If I feel the desk, I'm probably near the window." This mental map is crucial because our brain can't directly "see" our position—it has to figure it out indirectly through these learned associations.

        In the language of active inference, we call our actual position in the room a "hidden state" because it's something real but not directly observable. Think of it like this:

        - Hidden State: Your actual position (which you can't directly see)

        - Observations: The objects you can touch and recognize

        - Brain's Task: Using these observations to infer your hidden state

        Mathematically, we can think of this as a function f(s)=o that maps hidden states (s) to observations (o). It's like having a decoder ring that helps translate what we touch into information about where we are.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    A_matrix = mo.image(
        src=str(mo.notebook_location() / "public" / "A-matrix.png"),
        width="40%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )

    answer_a_matrix = mo.accordion(
        {
            "Answer:": f"{A_matrix}This matrix has dimensions [8x9], allowing us to explore various states and their related observations. In active inference this is called the “A matrix” or the probability of an observation given a (hidden) state, which can also be written as P(o|s)."
        }
    )
    hint_a_matrix = mo.accordion(
        {
            "Hint:": "focus on possible states(locations) and possible observations (objects)."
        }
    )
    question_a_matrix = mo.accordion(
        {
            "Question: How can we write this down as a matrix? Try to predict how this matrix should look like?": [
                hint_a_matrix,
                answer_a_matrix,
            ]
        }
    )
    mo.callout(question_a_matrix, kind="info")
    return A_matrix, answer_a_matrix, hint_a_matrix, question_a_matrix


@app.cell
def _(grid_locations):
    """ Create variables for the storing the dimensionalities of the hidden states and the observations """

    n_states = len(grid_locations)
    n_observations = len(grid_locations) -1 #since we only have 8 objects (the chair is doubled)

    print(f'Dimensionality of hidden states: {n_states}')
    print(f'Dimensionality of observations: {n_observations}')
    return n_observations, n_states


@app.cell
def _(n_observations, n_states, np):
    """ Create the A matrix  """

    A = np.zeros( (n_observations, n_states) )
    return (A,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Great. Now we need to feed it with some values.""")
    return


@app.cell(hide_code=True)
def _(mo):
    A_matrix_filled = mo.image(
        src=str(mo.notebook_location() / "public" / "A-matrix_filled.png"),
        width="60%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )

    answer_a_matrix_filled = mo.accordion(
        {
            "Answer:": f"{A_matrix_filled}This is how it looks like. Basically what this says is, being on field 0 we will observe a lamp to 100%."
        }
    )
    hint_a_matrix_filled = mo.accordion(
        {
            "Hint:": "look at the room plan. You can enter a 1 (equal to 100%) where each object is located on the field index."
        }
    )
    question_a_matrix_filled = mo.accordion(
        {
            "Question: Give each cell in the A matrix a value.": [
                hint_a_matrix_filled,
                answer_a_matrix_filled,
            ]
        }
    )
    mo.callout(question_a_matrix_filled, kind="info")
    return (
        A_matrix_filled,
        answer_a_matrix_filled,
        hint_a_matrix_filled,
        question_a_matrix_filled,
    )


@app.cell
def _(A, np):
    """ Create an unambiguous or 'noise-less' mapping between hidden states and observations """
    np.fill_diagonal(A, 1.0)  # Fill diagonal with 1's first

    # Modify specific columns to match desired observation mapping
    A[:, 6] = 0  # Clear column 6
    A[2, 6] = 1  # Set row 2, column 6 to 1 (equal to chair is on field 6)

    A[:, 7] = 0  # Clear column 7
    A[6, 7] = 1  # Set row 6, column 7 to 1

    A[:, 8] = 0  # Clear column 8
    A[7, 8] = 1  # Set row 7, column 8 to 1
    return


@app.cell
def _(A, plot_likelihood):
    plot_likelihood(A, title_str = "A matrix or $P(o|s)$")
    return


@app.cell(hide_code=True)
def _(mo):
    loop_a = mo.image(
        src=str(mo.notebook_location() / "public" / "loop-environment-agent_A_matrix.png"),
        width="40%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )

    answer_loop_a = mo.accordion(
        {"Answer:": f"{loop_a}between the room position and the observations."}
    )
    hint_loop_a = mo.accordion(
        {"Hint:": "which arrow connects hidden states with observations?"}
    )
    question_loop_a = mo.accordion(
        {
            "Question: Where in our action-perception loop should we place this matrix?": [
                hint_loop_a,
                answer_loop_a,
            ]
        }
    )

    mo.callout(question_loop_a, kind="info")
    return answer_loop_a, hint_loop_a, loop_a, question_loop_a


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Equipped with this nice matrix we can already try our fist inference.
        Let’s imagine we’re touching a chair. We store this observation in another array. This array will represent the likelihood of sensing each possible object. Since we are very sure it is a chair, we note it with a 1 for the chair (our observation) and 0 for everything else.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "observation_chair.png"),
        width="20%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell
def _(n_observations, np):
    # Create array with length of observations, initialize with zeros
    observation_chair = np.zeros(n_observations)
    # enter 1 in the field 2 (equal to chair)
    observation_chair[2]=1
    #print to control
    print(observation_chair)
    return (observation_chair,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Now, the fun begins. Let's see what we can infer from simply touching a chair and having our A matrix.

        To make this mathematically we combine the observation array with our A matrix using a dot product. The dot product essentially cross-references our observation with the A matrix, filtering out the states (positions) that don’t match our observation. It highlights the states where the chair is most likely located.

        To turn this result into an interpretable probability function, we take the natural logarithm of the outcome. This logarithmic transformation adjusts the values to emphasize differences in probabilities. Finally, we pass these adjusted values through a softmax function, which converts them into probabilities that sum to 1.

        The softmax function outputs something intuitive: the relative likelihood of being in each room position, given the observation of the chair. In other words, it tells us how confident we should be that we’re in a particular spot based on what we’ve touched.

        **Breaking It Down: Step-by-Step**
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "VFE_A.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(A, log_stable, observation_chair, softmax):
    # equal to first step/row of graphic
    dot_next_state = observation_chair.dot(A)
    print(f"o dot A={dot_next_state}")

    #equal to second step of graphic
    log_next_state = log_stable(dot_next_state)
    # we reshape it to display it like a column vector
    print(f"ln(next_state)={log_next_state.reshape(-1,1)}")

    next_state = softmax(log_next_state)
    print(f"next_state={next_state}")
    return dot_next_state, log_next_state, next_state


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        What does this result tell us? Touching a chair we assume to 50% that we are on the upper right corner (field 2) but also to 50% that we are on the lower left corner (field 6). That's a not too bad guess for the beginning, since by 50% chance we are correct, but yet we are still quite unsure where we are. So only relying on our current observation doesn't bring us too far -  we need something else.

        What could help? When we woke up we actually remembered we were on the bed, which we assumed to be somewhere on the lower left side of the room. Let's use this information, to make our guess of our position more precise.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Our first guess - "D Matrix"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        The only thing we need to do, is to store our current prediction of our position (hidden state) as an array - in active inference this is called the "D array". or prior belief over hidden states at the first timestep p(s).

        Remember we wake up, and immediately we assume to be on the position where the bed is. so the middle left field of the room (field 4). since we dont remember it maybe so precisely we will also include the lower left corner in our prediction. we assume to be on either one of these two fields.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    D_matrix = mo.image(
        src=str(mo.notebook_location() / "public" / "D_matrix.png"),
        width="15%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )

    answer_d = mo.accordion(
        {
            "Answer:": f"{D_matrix}This is how it looks like. Basically what this says is, being on field 0 we will observe a lamp to 100%."
        }
    )
    hint_d = mo.accordion(
        {"Hint:": "Check the field index of the bed and lower left corner chair."}
    )
    question_d = mo.accordion(
        {
            "Question: Given that information, how should the D Matrix look like?": [
                hint_d,
                answer_d,
            ]
        }
    )
    mo.callout(question_d, kind="info")
    return D_matrix, answer_d, hint_d, question_d


@app.cell
def _(n_states, np, plot_beliefs, utils):
    """ Create a D vector, basically a belief that the agent has about its own starting location """

    # Create array with length of observations, initialize with zeros
    D = np.zeros(n_states)

    # since we might be in bed (field 3) or in the lower left corner (field 6)
    D[3] = 1
    D[6] = 1

    # normalize values so that all values add up to 1
    D = utils.norm_dist(D)

    """ Let's look at the prior over hidden states """
    plot_beliefs(D, title_str = "Prior beliefs over states")
    return (D,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Great. Now let's redo our above calculation, inferring our position from our current observation PLUS our belief/prediction of our position.
        For our example we say we remember being on the lower left side of the room. So either on field 3 or 6 with equal probability.
        The formula we use is: q(s[t]​)=σ(ln(D[:]​)+ln(A[o,:]))​.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "VFE_A_D.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell
def _(D, log_next_state, log_stable, plot_beliefs, softmax):
    # equal to first step/row of graphic
    # dot_next_state = observation_chair.dot(A) # already calculated above

    #equal to second step of graphic
    log_D = log_stable(D)
    # log_next_state = log_stable(dot_next_state) # already calculated above

    # 3rd and 4th row of graphic, taking the softmax of the sum of D and guessed_state
    updated_state = softmax(log_D + log_next_state)
    print(f"updated_state={updated_state}")
    """ Let's look at the updated belief over hidden states """
    plot_beliefs(updated_state, title_str = "Updated beliefs over states")
    return log_D, updated_state


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Great. Now we are left with a very confident and correct belief of our current position - assuming to be in the lower left corner (field 6) by 100%.
        So what is next? Let's shortly recapitulate: we made an observation (touching the chair), used our previous guess of our location and got to a refined result of our precise location.

        There is acutally one step we kind of skipped in our previous exmple. The fact that before touching the chair, we needed to perform an action, moving to the lower left corner field. So now lets try to include this in our example.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Our action manual - "B Matrix"
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        The question we ask is: How do hidden states (the room positions) transition over time (e.g. from one moment (t=0) to the other (t=1))?
        A: in our case the room itself doesnt move, so the fields themselfes remain where they are. So our current position only depends on our actions, depending where we were before.

        Let's define 5 different possible actions for our example: actions = ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

        Now we need to think of how to set up our B Matrix, so that we can show the effect of each action on our location (the hidden states).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    B_matrix = mo.image(
        src=str(mo.notebook_location() / "public" / "B_matrix.png"),
        width="90%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )

    answer_b = mo.accordion(
        {
            "Answer:": f"{B_matrix}We need  to map the current state (t=0) to the next state (t=1) given our action (n=5). This leaves us with a 9x9 matrix for each action (5 times)."
        }
    )
    hint_b = mo.accordion(
        {"Hint:": "Check how many possible room fields we have."}
    )
    question_b = mo.accordion(
        {
            "Question: What dimensions should our B Matrix have?": [
                hint_b,
                answer_b,
            ]
        }
    )

    mo.callout(question_b, kind="info")
    return B_matrix, answer_b, hint_b, question_b


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Now we need to set it up for each action. Lets start with the most intuitive: when we actually don't move, "Stay".""")
    return


@app.cell(hide_code=True)
def _(mo):
    B_stay = mo.image(
        src=str(mo.notebook_location() / "public" / "B_stay.png"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    B_stay_example = mo.image(
        src=str(mo.notebook_location() / "public" / "B_stay_example.png"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )

    answer_b_s = mo.accordion(
        {
            "Answer:": f"{B_stay} The matrix shows, that if we stay, the field index of the previous moment (rows) is the same as the current moment (columns). <br> {B_stay_example}We can interpret this as the following: being currently on field 6 (= row index 6) performing the action ""Stay"" will bring us to field 6 (= highlighted column index in row 6)."
        }
    )
    hint_b_s = mo.accordion(
        {"Hint:": "If we stay on one field, how does it affect the position in the next moment?"}
    )
    question_b_s = mo.accordion(
        {
            "Question: Which value should each field get??": [
                hint_b_s,
                answer_b_s,
            ]
        }
    )

    mo.callout(question_b_s, kind="info")
    return B_stay, B_stay_example, answer_b_s, hint_b_s, question_b_s


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Great. Now lets do the same for moving "Right".

        To fill this out just consider the consequence of going right for each field.
        So imagine you start on field 0 at t=0. Where will you be after moving one step to the right? A: field 1 at t=1.

        The same logic applies to field 1 at t=0.

        We have one special case. What whene we are at one of the rightside fields e.g. on field 2? How does going one step to right look like in this case? A: Correct, it is not possible, we will remain on field 2 at t=1

        With these thoughts we can plot our "right"-action matrix:
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "B_right.png"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Now lets do the same for the left step.
        (Basically it is the same matrix just turned by 180°).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "B_left.png"),
        width="50%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""The same we do for the Up and Down actions.""")
    return


@app.cell(hide_code=True)
def _(mo):
    up = mo.image(
        src=str(mo.notebook_location() / "public" / "B_up.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    down = mo.image(
        src=str(mo.notebook_location() / "public" / "B_down.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    mo.hstack([up,down])
    return down, up


@app.cell
def _(grid_locations, np):
    actions = ["UP", "DOWN", "LEFT", "RIGHT", "STAY"]

    def create_B_matrix():
      B = np.zeros( (len(grid_locations), len(grid_locations), len(actions)) )

      for action_id, action_label in enumerate(actions):

        for curr_state, grid_location in enumerate(grid_locations):

          y, x = grid_location

          if action_label == "UP":
            next_y = y - 1 if y > 0 else y 
            next_x = x
          elif action_label == "DOWN":
            next_y = y + 1 if y < 2 else y 
            next_x = x
          elif action_label == "LEFT":
            next_x = x - 1 if x > 0 else x 
            next_y = y
          elif action_label == "RIGHT":
            next_x = x + 1 if x < 2 else x 
            next_y = y
          elif action_label == "STAY":
            next_x = x
            next_y = y
          new_location = (next_y, next_x)
          next_state = grid_locations.index(new_location)
          B[next_state, curr_state, action_id] = 1.0
      return B

    B = create_B_matrix()
    return B, actions, create_B_matrix


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        So our B matrix actually consists of 5x9x9 matrices or also called object array in pymdp or tensor in other Programming languages.

        Let’s now explore what it looks to “take” an action, using matrix-vector product of an action-conditioned “slice” of the  $\mathbf{B}$ array and a previous state vector.

        So remember we assumed we started on our bed. We convert this into its corresponding index (i=3) and then use a one-hot encoding vector, meaning that we render only the current position as 1 (all other fields as 0), just identical to the D matrix (in fact in the very beginning of our loop we will use the D matrix for this, since we havent performed any previous action. So its kind of used to initialize our loop).
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "current_state_3.png"),
        width="10%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell
def _(n_states, plot_beliefs, utils):
    """ Define a starting location""" 
    starting_location = 3

    """  and create a state vector out of it """
    starting_state = utils.onehot(starting_location, n_states)
    print(starting_state)
    plot_beliefs(starting_state, "Categorical distribution over the starting state")
    return starting_location, starting_state


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Then we calculate the next field at t=1 after having gone one step down. We can do this by using a matrix-vector product of the current state vector and the corresponding matrix for the "Down" action from our B Matrix.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "current_state_B.png"),
        width="60%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        You can think of this calculation as if we would move the current state vector step-wise over the B matrix slice, multiplying each overlying values. Then summing up the resulting values per each column.
        In our example this means: only keeping the fields white when both fields are white.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "current_state_B_result.png"),
        width="70%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell
def _(
    B,
    actions,
    grid_locations,
    plot_beliefs,
    plot_point_on_grid,
    starting_state,
):
    """ Generate the next state vector, given the starting state and the B matrix"""
    down_action_idx = actions.index("DOWN") 
    next_state_down = B[:,:, down_action_idx].dot(starting_state) # input the indices to the B matrix
    """ Plot the distribution of the vector"""
    plot_beliefs(next_state_down, "Categorical distribution over the starting state")

    """ Plot the next state, after taking the action over the grid """
    plot_point_on_grid(next_state_down, grid_locations)
    return down_action_idx, next_state_down


@app.cell(hide_code=True)
def _(mo):
    mo.md("""So moving one step down from field 3 brings us to field 6.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### Variational Inference Calculation - Where are we based on our observation?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Let's insert this calculation into our above procedure. So instead of using our predicted state (location). we will use our intial prior D (we are on the bed) as well as the corresponding B matrix slice for our planned action: going one step down.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "VFE_calculation.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell
def _(log_stable, next_state, next_state_down, plot_beliefs, softmax):
    # first row of graphic
    # use 
    updated_state_action = softmax(log_stable(next_state_down)+log_stable(next_state))
    print(updated_state_action)
    """ Plot the distribution of the vector"""
    plot_beliefs(next_state_down, "Categorical distribution over the starting state")

    return (updated_state_action,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Let's pause for a moment and summarize our journey through understanding how our brain figures out where we are in the dark room. We've discovered that this process combines three key elements:

        1. **Our Current Observations** (A Matrix)
           - When we touch objects in the room, our brain uses the A matrix like a lookup table
           - This matrix tells us which objects we might encounter at each possible location
           - For example, touching a chair narrows down our possible positions to locations where chairs exist

        2. **Our Initial Beliefs** (D Matrix)
           - We start with some prior knowledge (like remembering we fell asleep on the bed)
           - This initial belief is stored in our D matrix, representing our best guess before any new observations

        3. **Our Movement History** (B Matrix)
           - As we move around, the B matrix helps us track how our position changes
           - Each action (like stepping left or right) updates our possible location
           - This creates a continuous chain of position updates based on our movements

        These components work together in a beautiful mathematical dance: our brain combines the evidence from what we touch (through the A matrix) with our previous beliefs (from D or B matrices) to create an increasingly accurate picture of our location. This process of combining evidence with beliefs is exactly what we call Variational Free Energy minimization - it's our brain's way of solving the puzzle of where we are in the dark.

        Let's visualize how these elements fit into our perception-action loop:
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "loop-environment-agent-brain-detailed-VFE_matrices.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## 2. What is our best action? - Expected free energy (EFE)""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.sidebar(
        [
            mo.md("# Active Inference"),
            mo.nav_menu(
                {
                    "#/home": f"{mo.icon('lucide:home')} Home",
                    "#/reading": f"{mo.icon('lucide:book')} Reading",
                    "#/programming": f"{mo.icon('lucide:computer')} Programming",
                    "Links": {
                        "https://www.activeinference.institute/": "Active Inference Institute"
                    },
                },
                orientation="vertical",
            ),
        ]
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(n_observations, n_states, np, plt, sns):
    def plot_likelihood(matrix, xlabels = list(range(n_states)), ylabels = list(range(n_observations)), title_str = "Likelihood distribution (A)"):
        """
        Plots a 2-D likelihood matrix as a heatmap
        """

        if not np.isclose(matrix.sum(axis=0), 1.0).all():
          raise ValueError("Distribution not column-normalized! Please normalize (ensure matrix.sum(axis=0) == 1.0 for all columns)")

        fig = plt.figure(figsize = (6,6))
        ax = sns.heatmap(matrix, xticklabels = xlabels, yticklabels = ylabels, cmap = 'gray', cbar = False, vmin = 0.0, vmax = 1.0)
        plt.title(title_str)
        plt.show()

    def plot_grid(grid_locations, num_x = 3, num_y = 3 ):
        """
        Plots the spatial coordinates of GridWorld as a heatmap, with each (X, Y) coordinate 
        labeled with its linear index (its `state id`)
        """

        grid_heatmap = np.zeros((num_x, num_y))
        for linear_idx, location in enumerate(grid_locations):
          y, x = location
          grid_heatmap[y, x] = linear_idx
        sns.set(font_scale=1.5)
        sns.heatmap(grid_heatmap, annot=True, cbar = False, fmt='.0f', cmap='crest')
        plt.show()

    def plot_point_on_grid(state_vector, grid_locations):
        """
        Plots the current location of the agent on the grid world
        """
        state_index = np.where(state_vector)[0][0]
        y, x = grid_locations[state_index]
        grid_heatmap = np.zeros((3,3))
        grid_heatmap[y,x] = 1.0
        sns.heatmap(grid_heatmap, cbar = False, fmt='.0f')
        plt.show()

    def plot_beliefs(belief_dist, title_str=""):
        """
        Plot a categorical distribution or belief distribution, stored in the 1-D numpy vector `belief_dist`
        """

        if not np.isclose(belief_dist.sum(), 1.0):
          raise ValueError("Distribution not normalized! Please normalize")

        plt.grid(zorder=0)
        plt.bar(range(belief_dist.shape[0]), belief_dist, color='r', zorder=3)
        plt.xticks(range(belief_dist.shape[0]))
        plt.title(title_str)
        plt.show()
    return plot_beliefs, plot_grid, plot_likelihood, plot_point_on_grid


@app.cell(hide_code=True)
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from pymdp.maths import softmax
    from pymdp.maths import spm_log_single as log_stable
    return log_stable, np, plt, sns, softmax


if __name__ == "__main__":
    app.run()
