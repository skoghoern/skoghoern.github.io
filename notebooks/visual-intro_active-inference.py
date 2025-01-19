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
    mo.md(r"""May I welcome you as a guest in my little room? This is where I sleep, study, watch Tv etc. Now we might all know this situation, we are in bed and suddenly we get very hungry. We want these yummy cookies that we left on the table before. The only problem - the light is turned off. We might have all been in such a situation already. How do we get to the cookies only moving in the dark? Yes we start being a zombie, hands out and trying to touch everything around us, to get a clue where we currently are. we might touch something metallic - ouch that was the trash bin in the corner. we might feel something soft beneath our feet - yes that's the carpet in the middle of the room. We know that the table where we left the cookies is just upfront. we go two little steps and yep, knock on something wooden and a moment later we have that cookie box in our hand that we were craving for. Yummy!""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Active Inference Loop""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Let's explore how did this actually work? Let's try to simulate what seemed relatively intuitive and what we do every day.
        Let’s consider how we can illustrate the process of us staggering through the room. What is actually happening? What elements do we need to recreate this situation?
        As already in the question: there are two elments: us and the room that interact with each other. We will plot it more generically, where us can be any active agent and the room can be any environment.
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
    mo.md(r"""### 1. The enviornment - the world""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""When we think of our room there are two main variables that define it closer: the objects in the room that we can touch, and the position in the room. Since each object has a room position, those two variables are connected.""")
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
    mo.md("""### 2. The agent - us as person""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Let’s take a closer look to our agent, ourselves in this case. Can we subdivide our being into smaller building blocks?
        I will propose that we can subdivide us in three main variables.

        #### 2.1. Observation/Perception states
        As we already stated in the environment part, there are the objects that we can touch. They ultimately become our observation states. For simplicity reasons these will be equal to the objects that we have in the room, assuming that we immediately know what object it is, by touching it.
        #### 2.2. Brain
        These information get send to our brain, located in a dark cave in our head. There it performes some calculations with the new obtained information, trying to understand where we are and what we need to do to get to our cookies. We will depict this calculation in our sketch below by the small boxes inside the brain.
        #### 2.3. Action
        And this directly brings us to our last variable: the actions that we perform based on our brains calculations. In our case this will be the movements we can do: going right, left, up or down. Ultimately changing our position in the room.
        """
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
        r"""
        We have gathered all necessary variables for the moment. Now let’s try to arrange them in a meaningful way.
        Based on our current room position, we will have ceratain objects around us. while we can directly observe our room position in the dark, we can touch the objects. These will generate our observations. The observations then get send to our brain where we do some calculations. and finally decide to make an action, which to keep it simple, will only be our possible movements in the room. Thus changing our room postion. Which will generate new observations based on the objects around us and so on. The loop is closed.

        This is the main concept active inference relies upon. Everything from now will build up on this, refine part of it or scale it. But you already have the main idea of how our brain works.
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
        Now how can we bring this into something that our computer can work with? We need to further abstract this scheme and  introduce some numbers and tables that our computer understands well.

        To start off, let's try to abstract the image of my little room above into a reduced version, by drawing it down similar to a floor plan and arbitrarily dividing it into a 3x3 (3 times 3) grid. We provide each field with an index.
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
    mo.md("""## 1. Understanding where we are - Variational Free Energy""")
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
        Let’s focus on how we figure out where we are in the room. In our dark-room cookie quest, we relied on touch. By recognizing objects—like the trash bin, carpet, or table—we deduced our position. Our brain didn’t have a "bird’s-eye view" of the room. Instead, it worked like a detective, piecing together clues from what we touched (our observations) to infer our location (our state). To be able to do this it needed a certain map or cheat sheet, where it can look up, what being in touch with a certain object implies about the current room position, that the person is currently in. Since the brain doesn’t have direct access to the current position in the room, we will call them, as in active inference models typical, hidden states.

        A hidden state represents the actual situation you’re in but can’t directly see or know—like your precise position in the dark. What you do have are observations (e.g., touching the table or the bed). To infer your hidden state from observations, your brain uses a model of how the world works.

        So basically our brain evolves a function of the hidden states in respect to the observations. f(s)=o mapping each observation to a certain state.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Great. Now we need to feed it with some values.""")
    return


@app.cell(hide_code=True)
def _(mo):
    A_matrix_filled = mo.image(
        src=str(mo.notebook_location() / "public" / "A-matrix_filled.png"),
        width="40%",
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
    mo.md(
        """

        Let's insert this calculation into our above procedure. So instead of using our predicted state (location). we will use our intial prior D (we are on the bed) as well as the corresponding B matrix slice for our planned action: going one step down.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        src=str(mo.notebook_location() / "public" / "VFE_calculation.png"),
        width="100%",
        style={"display": "block", "margin": "0 auto"},  # CSS for centering
    )
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


if __name__ == "__main__":
    app.run()
