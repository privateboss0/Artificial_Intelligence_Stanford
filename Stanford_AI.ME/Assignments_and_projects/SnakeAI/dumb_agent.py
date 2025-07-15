import gymnasium as gym
from Snake_EnvAndAgent import SnakeGameEnv
import pygame
import time

if __name__ == "__main__":

    env = SnakeGameEnv(render_mode='human')

    episodes = 10
    for episode in range(episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0
        steps = 0

        print(f"--- Starting Episode {episode + 1} ---")

        while not done:
            # For manual testing
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_UP]: action = 0 (map to straight)
            
            action = env.action_space.sample() # Randomly chooses 0, 1, or 2

            next_obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
            steps += 1
            done = terminated or truncated

            # Render the environment
            #env.render()
            #time.sleep(100) # Small delay to see the game progression

            obs = next_obs # Update observation for next step

        print(f"Episode {episode + 1} finished in {steps} steps with total reward: {total_reward:.2f}")
        print(f"Final Score: {info['score']}")

    env.close()
    print("Environment test finished.")
