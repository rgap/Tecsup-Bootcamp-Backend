import { CheckCircleIcon, TrashIcon } from "@heroicons/react/24/solid";
import { Card, DeleteTask, Edit } from "../../components";

/* eslint-disable react/prop-types */
export default function Task({ task, getTasks }) {
  return (
    <Card className="mt-5 flex justify-between">
      <p>{task.title}</p>
      <div className="flex gap-3">
        <CheckCircleIcon className="h-6 w-6 text-green-500" />
        <Edit task={task} getTasks={getTasks} />
        <DeleteTask task={task} getTasks={getTasks} />
        {/* <TrashIcon className="h-6 w-6 text-blue-500" /> */}
      </div>
    </Card>
  );
}
