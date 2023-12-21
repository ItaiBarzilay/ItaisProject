import pyglet

# Create a window
window = pyglet.window.Window(800, 600)

# # Load card images (you'll need to have card images in the same directory)
# card_images = [pyglet.image.load(f'card{i}.png') for i in range(1, 3)]
# # Create sprite objects for the cards
# cards = [pyglet.sprite.Sprite(img) for img in card_images]

# # Set the initial positions for the cards
# for i, card in enumerate(cards):
#     card.x = 100 + i * 100
#     card.y = 500

# # Define an update function for animation
# def update(dt):
#     for card in cards:
#         card.x += 1  # Move the cards horizontally
#         if card.x > window.width:
#             card.x = -card.width  # Reset cards when they go off the screen
#
# # Register the update function
# pyglet.clock.schedule_interval(update, 1/60.0)


# Create sprite objects for the cards
cards = [pyglet.sprite.Sprite(pyglet.image.load(f'card0.png')) for i in range(1, 20)]
# # Set the initial positions for the cards
for i, card in enumerate(cards):
    card.x = 300 + i
    card.y = 450 - 2 * i


# # Define an update function for animation
def update(dt,place):
     cards[place].y -= 1  # Move the cards horizontally
     print(cards[place].y)
     if cards[place].y < 100:
         pyglet.clock.unschedule(update)  # Stop the update loop when all cards are gone

# Register the update function
for i in range(-1,-4):
    pyglet.clock.schedule_interval(update, 1/200.0,i)
    cards[i].x = i * 100

@window.event
def on_draw():
    window.clear()
    for card in cards:
        card.draw()

if __name__ == "__main__":
    pyglet.app.run()
