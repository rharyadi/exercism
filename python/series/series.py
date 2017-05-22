def slices(numbers,slice_width):
    numbers = [int(d) for d in numbers]

    if slice_width > len(numbers) or not slice_width:
        raise ValueError

    series = []
    for i in range(0,len(numbers)-slice_width+1):
        series.append(numbers[i:i+slice_width])
    
    return series
    
