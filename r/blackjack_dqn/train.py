def train(episode_num, env, eval_env, evaluate_every, evaluate_num, agent, logger, tournament):
   for episode in range(episode_num):
     
     # Generate data from the environment
     trajectories, _ = env.run(is_training = True)

     # Feed transitions into agent memory, and train the agent
     for ts in trajectories[0]:
         agent.feed(ts)

     # Evaluate the performance. Play with random agents.
     if episode % evaluate_every == 0:
         logger.log_performance(env.timestep, tournament(eval_env, evaluate_num)[0])
