def attach_images(observations, images):
    for i, obs in enumerate(observations):
        if i < len(images):
            obs["image"] = images[i]
        else:
            obs["image"] = "Image Not Available"
    return observations