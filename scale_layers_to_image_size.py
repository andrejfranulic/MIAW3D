from gimpfu import *

def scale_layers_to_image_size(image, drawable):
    pdb.gimp_image_undo_group_start(image)
    try:
        # Get the dimensions of the image
        image_width = pdb.gimp_image_width(image)
        image_height = pdb.gimp_image_height(image)

        # Get the list of layers
        layers = image.layers

        for layer in layers:
            if pdb.gimp_item_is_layer(layer):
                # Scale the layer to the size of the image
                pdb.gimp_layer_scale(layer, image_width, image_height, False)
    except Exception as e:
        pdb.gimp_message("An error occurred: " + str(e))
    finally:
        pdb.gimp_image_undo_group_end(image)

register(
    "python_fu_scale_layers_to_image_size",
    "Scale each layer to the size of the image",
    "Scale each layer to the size of the image",
    "Your Name",
    "Your Name",
    "2024",
    "<Image>/Layer/Scale Layers to Image Size",
    "*",
    [],
    [],
    scale_layers_to_image_size)

main()
