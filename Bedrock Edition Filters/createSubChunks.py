#Written by gentlegiantJGC
#http://youtube.com/gentlegiantJGC
#https://twitter.com/gentlegiantJGC

# if you are going to use the code in this filter please give credit

# Note PE/Windows 10... (Bedrock Edition) only
# This filter was written to create sub-chunks in MCedit that have not been created by the game
# MCedit will allow you to paste/clone/fill in sub-chunks that have not been created but they will
# not get written to disk because the sub-chunk was technically never created in MCedit

displayName = "Create Sub-Chunks"

inputs = (
	("Unmodified sub-chunks are not saved", "label"),
	("to disk. This filter will create", "label"),
	("sub-chunks in and below the selection", "label"),
	)
	
def perform(level, box, options):
	# terrain tag in the format (version x1, blocks (air) x4096, block data x4096*0.5) 
	terrain = '\x00'+'\x00'*4096+'\x00'*2048
	# iterating through every chunk in the box
	for cx, cz in box.chunkPositions:
		try:
			# get the chunk object
			chunk = level.getChunk(cx, cz)
		except:
			# if the whole chunk does not exist then continue to the next one
			# the chunk probably could be generated within MCedit but it wouldn't contain any terrain
			# and I don't know how the game would deal with it.
			# It may regerate the chunk since it is empty or might leave it as it is
			print 'issue loading chunk ('+str(cx)+', '+str(cz)+'). Go near it in game to genearate terrain'
			continue
		# for every chunk up to the top of the selection box
		for i in range(1+box.maxy/16):
			# if the sub-chunk does not already exist
			if i not in chunk.subchunks:
				# create it with the terrain value created earlier
				chunk.add_data(terrain=terrain, subchunk=i)
		# tell MCedit the chunk has changed
		chunk.dirty = True
