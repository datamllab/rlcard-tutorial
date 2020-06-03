def train(episode_num, env, eval_env, evaluate_every, evaluate_num, agent, logger, tournament):
    for episode in range(episode_num):
    	agent.train()
    	print('\rIteration {}'.format(episode), end='')
        # Evaluate the performance. Play with NFSP agents.
    	if episode % evaluate_every == 0:
        	agent.save() # Save model
        	logger.log_performance(env.timestep, tournament(eval_env, evaluate_num)[0])
