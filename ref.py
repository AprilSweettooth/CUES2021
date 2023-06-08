from collections import Counter
word = 'Lorem ipsum dolor sit amet consectetur adipiscing elit Pellentesque eu ex finibus tortor faucibus vulputate. Suspendisse nec mauris feugiat, congue libero in, condimentum magna. Suspendisse facilisis id massa imperdiet consequat. Aliquam lacinia feugiat quam, at luctus nulla condimentum pulvinar. Donec fermentum quam placerat mi tristique sollicitudin. Phasellus eros quam, volutpat ullamcorper sodales dapibus, sollicitudin sed quam. Donec tincidunt bibendum justo vitae luctus. Suspendisse tincidunt magna egestas metus consequat tincidunt. Donec cursus cursus leo, tincidunt accumsan eros. Integer in fringilla nisl, vel fermentum tortor. Aliquam luctus turpis nec tortor cursus, commodo tempor odio pharetra. Aliquam consequat purus iaculis sapien mollis, vel sagittis metus dictum. Integer tempus mauris ac magna pharetra, vel fringilla tellus rutrum. Phasellus congue ipsum quis lacus pellentesque consectetur vitae nec est. Aliquam consequat luctus dolor pulvinar tempus. Phasellus sed massa turpis Etiam porttitor leo non commodo rutrum. Vestibulum ultricies, ligula vitae hendrerit facilisis, ipsum neque finibus erat, non suscipit ante odio non nisi. Nulla nec dui tincidunt, fermentum nunc et, sodales nisi. Donec a nibh at ante pharetra dapibus. Integer arcu mi, consectetur nec ante id, fermentum placerat felis. Mauris orci elit, vestibulum nec fermentum vitae, consequat ac sem. Mauris dictum quam ante, eget vestibulum turpis molestie ut Nulla lacinia nisi leo, eget porttitor massa accumsan et. Aenean diam urna, ornare eu gravida in, sodales quis ante. Maecenas rhoncus, libero vel ultrices aliquam, ipsum lectus malesuada nisl, sed efficitur nibh leo ac odio. In eget maximus arcu, venenatis hendrerit dolor. Integer condimentum purus et nisi tempus, et accumsan orci semper. Aliquam sed dapibus neque, in consectetur risus. In eros dolor, vulputate vel nisl nec, congue rhoncus mauris. Vestibulum ac magna aliquam, egestas quam quis, porta purus. Donec pulvinar in elit eget finibus. Cras feugiat est eget dapibus iaculis. Aenean imperdiet quis lorem eu suscipit. Phasellus vel porttitor ex, at fringilla felis. Curabitur non finibus massa. Nulla dolor mi, dictum ultrices purus in, dignissim venenatis odio. Aenean sed egestas nisi. Praesent ac diam maximus, ultrices lectus quis, condimentum turpis. In eu ipsum at metus eleifend accumsan id sit amet velit. Cras molestie sit amet est vitae faucibus. Maecenas porttitor sit amet tellus et sollicitudin. Donec maximus euismod lacinia. Maecenas efficitur elit libero, eu interdum lectus vestibulum id. Proin non eros orci. Vivamus at arcu vitae mi sagittis vestibulum eu in enim. Morbi elementum odio justo, et fermentum sapien cursus vel. Cras suscipit venenatis eros interdum interdum. Nunc sit amet velit ac dui pharetra tincidunt. Praesent ornare justo vel feugiat lobortis. In sit amet massa vel arcu imperdiet efficitur ac quis nunc. Proin tristique ornare ante varius molestie. Curabitur vel magna enim. Duis id gravida dui, et consectetur elit. Aliquam efficitur dui at justo congue rutrum. Duis sed suscipit lorem. Etiam ut feugiat augue. Curabitur condimentum, urna vitae malesuada dictum, velit mauris varius erat, vitae rutrum tellus dui at diam. Curabitur nec tristique urna, eget varius metus. Vestibulum in augue a ligula malesuada tincidunt nec non eros. Morbi vel rhoncus augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ac aliquam eros.'

counts = Counter(word)  # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
count = 0
for i in word:
    count += counts(i)
for i in word:
    print(i, counts[i]/count)
