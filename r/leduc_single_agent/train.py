def train(timesteps, env, eval_env, evaluate_every, evaluate_num, agent, logger,state):
    import numpy as np
    for timestep in range(timesteps):
        print(type(state))
        print(state)
        action = agent.step(state)
        next_state, reward, done = env.step(action)
        ts = (state, action, reward, next_state, done)
        agent.feed(ts)

        if timestep % evaluate_every == 0:
            rewards = []
            state = eval_env.reset()
            for _ in range(evaluate_num):
                action, _ = agent.eval_step(state)
                _, reward, done = env.step(action)
                if done:
                    rewards.append(reward)
            logger.log_performance(env.timestep, np.mean(rewards))

