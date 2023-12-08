def calculate_score(tasks, consistency, account_age, screen_time, task_retention):
    # Define weight factors for each criterion
    weight_tasks = 0.15
    weight_consistency = 0.35
    weight_account_age = 0.2
    weight_screen_time = 0.1
    weight_task_retention = 0.2

    # Normalize each criterion to a scale from 0 to 1
    normalized_tasks = min(tasks / 21, 1)  # Max number of tasks
    normalized_consistency = consistency  # How consistently the tasks are completed
    normalized_account_age = min(account_age / 365, 1)  # Account age in days
    normalized_screen_time = min(screen_time / 15000, 1)  # Screen time in seconds
    normalized_task_retention = task_retention  # Reward for infrequent task removal

    # Calculate the weighted score
    score = (
        weight_tasks * normalized_tasks +
        weight_consistency * normalized_consistency +
        weight_account_age * normalized_account_age +
        weight_screen_time * normalized_screen_time +
        weight_task_retention * normalized_task_retention
    )

    # Scale the score to the range from 300 to 850
    min_score = 300
    max_score = 850
    accountability_score = int(min_score + (max_score - min_score) * score)

    return accountability_score