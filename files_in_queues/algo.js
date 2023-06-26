const files = [
	8, 5, 8, 2, 3, 5, 7, 7, 9, 16, 9, 8, 7, 68, 6, 9, 86, 8, 4, 8, 4, 8, 94, 6, 8,
	9, 36, 9, 36, 9, 8, 3, 46, 8, 9, 34, 9,
];

function UploadToCloud(files) {
	const images = [];
	files.map((file) => images.push(file * 2));
	return images;
}

console.log(UploadToCloud(files));
