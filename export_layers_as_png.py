from gimpfu import *

def export_layers_as_png(image, drawable, output_folder):
    pdb.gimp_image_undo_group_start(image)
    try:
        # Ensure the output folder ends with a slash
        if not output_folder.endswith('/'):
            output_folder += '/'

        # Get the list of layers
        layers = image.layers

        for layer in layers:
            if pdb.gimp_item_is_layer(layer):
                # Get the layer name
                layer_name = layer.name
                # Replace spaces and other potentially problematic characters
                safe_layer_name = layer_name.replace(' ', '_').replace('/', '_')
                # Create the output file path
                output_file = output_folder + safe_layer_name + ".png"
                # Duplicate the layer and create a new image with it
                new_image = pdb.gimp_image_new(layer.width, layer.height, image.base_type)
                new_layer = pdb.gimp_layer_new_from_drawable(layer, new_image)
                pdb.gimp_image_add_layer(new_image, new_layer, 0)
                # Export the new image as PNG
                pdb.file_png_save(new_image, new_layer, output_file, output_file, 0, 9, 0, 0, 0, 0, 0)
                # Clean up
                pdb.gimp_image_delete(new_image)
    except Exception as e:
        pdb.gimp_message("An error occurred: " + str(e))
    finally:
        pdb.gimp_image_undo_group_end(image)

register(
    "python_fu_export_layers_as_png",
    "Export each layer as a PNG file with the layer name",
    "Export each layer as a PNG file with the layer name",
    "Your Name",
    "Your Name",
    "2024",
    "<Image>/File/Export Layers as PNG",
    "*",
    [
        (PF_DIRNAME, "output_folder", "Output folder", "/tmp")
    ],
    [],
    export_layers_as_png)

main()
