from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    g_stack = []
    map_obj = {}
    for el in nums2[::-1]:
    	if not len(g_stack):
    		g_stack.append(el)
    		map_obj[el] = -1
    	elif len(g_stack):
	    	while len(g_stack) and el > g_stack[-1]:
	    		g_stack.pop(-1)
    		if not len(g_stack):
    			g_stack.append(el)
    			map_obj[el] = -1
    		else:
    			map_obj[el] = g_stack[-1]
    	else:
    		pass
    	g_stack.append(el)

    return [map_obj[n] for n in nums1]

nextGreaterElement([4,1,2] , [1,3,4,2])