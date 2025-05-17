import gradio as gr
import random

meal_data = {
    "Low Sodium": {
        "Breakfast": [
            "Oatmeal (made with water or low-sodium milk) with fresh berries and a sprinkle of cinnamon.",
            "Scrambled eggs with chopped unsalted vegetables like bell peppers, onions, and spinach.",
            "Plain Greek yogurt topped with sliced peaches and a drizzle of honey.",
            "Low-sodium cottage cheese with pineapple chunks and a side of melba toast (unsalted).",
            "Smoothie with unsweetened almond milk, spinach, banana, and unsalted almond butter.",
            "Whole-wheat pancakes or waffles made from scratch topped with fresh fruit and maple syrup.",
            "Chia seed pudding topped with raspberries and slivered almonds."
        ],
        "Lunch": [
            "Grilled chicken salad with mixed greens, cucumber, cherry tomatoes, and homemade vinaigrette.",
            "Tuna salad (canned tuna rinsed) mixed with plain Greek yogurt, celery, and onions in lettuce cups.",
            "Lentil soup with no-salt-added broth, lentils, carrots, celery, onions, and herbs.",
            "Quinoa salad with black beans, corn, bell peppers, cilantro, and lime-cumin dressing.",
            "Turkey and vegetable wrap with lettuce, tomato, cucumber, and hummus in a low-sodium tortilla.",
            "Baked cod with lemon, dill, pepper, steamed green beans, and baked sweet potato.",
            "Vegetable stir-fry with tofu and homemade low-sodium sauce."
        ],
        "Dinner": [
            "Baked salmon with dill, lemon juice, roasted asparagus, and brown rice.",
            "Lean ground turkey meatballs in low-sodium tomato sauce over whole-wheat pasta.",
            "Chicken and vegetable skewers with couscous.",
            "Pork tenderloin roasted with herbs, mashed cauliflower, and steamed carrots.",
            "Stuffed bell peppers with lean ground beef or lentils, rice, onions, tomatoes, and herbs.",
            "Homemade low-sodium pizza with tomato sauce, part-skim mozzarella, and fresh vegetables.",
            "Black bean burgers on low-sodium buns with lettuce, tomato, and baked sweet potato fries."
        ],
        "Snacks": [
            "A handful of unsalted almonds or walnuts.",
            "Apple slices with unsalted almond butter.",
            "Plain rice cakes with avocado.",
            "Fresh berries.",
            "Cucumber slices with dill.",
            "Low-sodium whole-wheat crackers.",
            "Plain Greek yogurt."
        ]
    },
    "Low Potassium": {
        "Breakfast": [
            "Rice Krispies or Corn Flakes with rice milk or low-fat cow's milk with blueberries.",
            "White toast with unsalted butter and jelly.",
            "Scrambled egg whites with bell peppers and onions with a small portion of grits.",
            "Pancakes with apple slices (peeled) and light syrup.",
            "Cream of rice cereal with cinnamon and cranberries.",
            "Bagel with cream cheese.",
            "Refined wheat cereals with suitable milk and low-potassium fruit."
        ],
        "Lunch": [
            "Chicken salad sandwich with cooked chicken, mayonnaise, celery, and peeled apple on white bread.",
            "Tuna salad with mayonnaise and cucumber on soda crackers.",
            "Pasta salad with cucumber, bell peppers, and light Italian dressing.",
            "Egg salad sandwich on white bread.",
            "Clear broth soup with noodles and green beans or carrots.",
            "Cottage cheese with canned peaches or pears.",
            "Turkey sandwich with lettuce, cucumber, and cranberry sauce."
        ],
        "Dinner": [
            "Baked chicken breast with herbs, white rice, and steamed green beans or cauliflower.",
            "Lean ground beef patty with noodles and boiled cabbage.",
            "Baked cod with lemon juice, white rice, and cooked carrots.",
            "Roast turkey slices with low-potassium gravy, mashed white potatoes, or white rice.",
            "Pasta with olive oil, garlic, chicken pieces, and bell peppers.",
            "Baked pork chop with applesauce and white rice.",
            "Shrimp scampi over refined pasta."
        ],
        "Snacks": [
            "Small peeled apple or apple slices.",
            "Small peeled pear.",
            "Handful of blueberries or raspberries.",
            "Cucumber slices.",
            "Low-potassium crackers like water biscuits.",
            "Rice pudding made with low-potassium milk.",
            "Canned peaches or pears in light syrup."
        ]
    },
    "Controlled Protein": {
        "Breakfast": [
            "Oatmeal with a small amount of berries.",
            "Whole-wheat toast with avocado.",
            "Rice porridge with green onions.",
            "Fruit salad with non-dairy whipped topping.",
            "Cornflakes with low-protein milk alternative.",
            "Half grapefruit with a small whole-wheat muffin.",
            "Vegetable omelet with one egg and low-protein vegetables."
        ],
        "Lunch": [
            "Large vegetable salad with mixed greens and a small portion of grilled chicken or chickpeas.",
            "Vegetable soup with a slice of bread.",
            "Rice noodles with stir-fried vegetables and small amount of tofu or shrimp.",
            "Sandwich with lettuce, tomato, cucumber, and hummus.",
            "Baked sweet potato with steamed broccoli and olive oil.",
            "Quinoa with roasted vegetables.",
            "Pasta with marinara sauce and cooked vegetables."
        ],
        "Dinner": [
            "Vegetable curry with coconut milk and white rice.",
            "Roasted vegetables with a small side of lean protein.",
            "Spaghetti squash with vegetable-rich tomato sauce.",
            "Eggplant parmesan with limited cheese.",
            "Stir-fry with rice or noodles and mostly vegetables with small protein.",
            "Lentil shepherd's pie with mashed cauliflower topping.",
            "Mushroom risotto with minimal cheese."
        ],
        "Snacks": [
            "Carrot or celery sticks.",
            "Small apple or pear.",
            "Rice crackers or melba toast.",
            "Low-protein fruit like berries or grapes.",
            "Cucumber slices with herbs.",
            "Small gelatin-based dessert.",
            "Unsalted popcorn."
        ]
    }
}

def get_meal_plan(diet_restriction):
    if diet_restriction not in meal_data:
        return "Invalid diet selection. Please choose from the available options."
    
    selected_diet = meal_data[diet_restriction]

    breakfast = random.choice(selected_diet["Breakfast"])
    lunch = random.choice(selected_diet["Lunch"])
    dinner = random.choice(selected_diet["Dinner"])
    snack = random.choice(selected_diet.get("Snacks", ["No snack suggestions available."]))

    plan = (
        f"Breakfast:\n{breakfast}\n\n"
        f"Lunch:\n{lunch}\n\n"
        f"Dinner:\n{dinner}\n\n"
        f"Snack:\n{snack}"
    )
    return plan

iface = gr.Interface(
    fn=get_meal_plan,
    inputs=gr.Dropdown(
        label="Select Your Diet Restriction Focus",
        choices=["Low Sodium", "Low Potassium", "Controlled Protein"],
        value="Low Sodium"
    ),
    outputs=gr.Textbox(label="Meal Suggestions", lines=20),
    title="Simple Kidney-Friendly Meal Planner",
    description="Select your diet restriction and get a sample daily meal plan."
)

if __name__ == "__main__":
    iface.launch()
